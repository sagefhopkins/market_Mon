import ConfigParser
import io
import json_Controller as jsc
import database_Controller as dbc
import time
from colorama import init, Fore, Back, Style
import threading
import re
import api_Key_Update as aku
from sys import stdout

def config_Add_Cur(currency):
    conf = open('config.ini', w)

    config = ConfigParser.ConfigParser()
    config.add('currency', currency, True)

    print (currency + " added to config.ini")

def config_Load_Cur():
    var = 0
    api_Key_Num = 1
    api_Key = ''
    class Thread(threading.Thread):
        def run(self):
            whileloop = 1
            while whileloop == 1:
                try:
                    #Check this crazy shit, I have no idea if this will actually work for storing variables in a non shared memory space
                    data = jsc.json_Import_Cur(re.sub('Thread-', '', threading.current_thread().name), api_Key)
                    final = jsc.regex_Seperate(data)
                    name = (re.sub('Thread-', '' , threading.current_thread().name))
                    dbc.database_Insert(name, final[0], final[1], final[2], final[3])
                    print (Fore.GREEN + "-------------------------------------------------------------------------------------------")
                    print (Back.WHITE + Style.DIM + Fore.CYAN  + final[0] + Style.NORMAL + Fore.YELLOW + final[1]  + Fore.MAGENTA + Back.WHITE + final[2] + Fore.RED + Back.WHITE + final[3] + Fore.BLUE + Back.WHITE +" inserted into database" + Style.RESET_ALL)
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
                    try:
                        api_Key_Array = aku.new_Key_Pull(api_Key_Num)
                        while api_Key_Array[0] == 'False':
                            api_Key_Num = api_Key_Num + 1
                            api_Key_Array = aku.new_Key_Pull(api_Key_Num)
                    except(TypeError):
                        pass
                    api_Key = api_Key_Array[1]
                    print api_Key
                    var = var + 1
                    currency = each_key
                    thread = Thread(name = "Thread-{}".format(each_key), kwargs = {each_key: currency})
                    thread.start()
                else:
                    time.sleep(4)
                    print (Fore.GREEN + "-------------------------------------------------------------------------------------------")
                    print (Fore.YELLOW + "Waitng for cooldown on throttle")
                    t = 60
                    while t:
                        stdout.write('\r\x1b[K'+t.__str__())
                        time.sleep(1)
                        stdout.flush()
                        t -= 1
                    var = 0
