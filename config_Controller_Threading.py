import ConfigParser
import io
import json_Controller as jsc
import database_Controller as dbc
import time
from colorama import init, Fore, Back, Style
import threading
import re
import sys
from __future__ import print_function

def config_Add_Cur(currency):
    conf = open('config.ini', w)

    config = ConfigParser.ConfigParser()
    config.add('currency', currency, True)

    print currency + " added to config.ini"

def config_Load_Cur():
    var = 0
    class Thread(threading.Thread):
        def run(self):
            whileloop = 1
            while whileloop == 1:
                try:

                    #Check this crazy shit, I have no idea if this will actually work for storing variables in a non shared memory space
                    data = jsc.json_Import_Cur(re.sub('Thread-', '', threading.current_thread().name))
                    final = jsc.regex_Seperate(data)
                    dbc.database_Insert('cur_Mon', final[0], final[1], final[2], final[3])
                    print Fore.GREEN + "-------------------------------------------------------------------------------------------"
                    print Back.WHITE + Style.DIM + Fore.CYAN  + final[0] + Style.NORMAL + Fore.YELLOW + final[1]  + Fore.MAGENTA + Back.WHITE + final[2] + Fore.RED + Back.WHITE + final[3] + Fore.BLUE + Back.WHITE +" inserted into database" + Style.RESET_ALL
                    time.sleep(1)
                    whileloop = 0
                except(IOError, TypeError, KeyError):
                    time.sleep(3)

    with open('config.ini') as f:
        conf = f.read()
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(conf))
        for each_section in config.sections():
            for (each_key, each_val) in config.items(each_section):
                if var != 5:
                    var = var + 1
                    print var
                    currency = each_key
                    thread = Thread(name = "Thread-{}".format(each_key), kwargs = {each_key: currency})
                    print "Starting Thread-{}".format(each_key)
                    thread.start()
                    time.sleep(2)
                else:
                    print "Waitng for cooldown on throttle"
                    t = 62
                    while t:
                        mins, secs = divmod(t, 60)
                        timeformat = '{:02d}:{:02d}'.format(mins, secs)
                        print(timeformat, end='\r')
                        time.sleep(1)
                        t -= 1
                    var = 0
