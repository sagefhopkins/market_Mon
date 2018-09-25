import ConfigParser
import io
import json_Controller as jsc
import database_Controller as dbc
import time
from colorama import init, Fore, Back, Style


def config_Add_Cur(currency):
    conf = open('config.ini', w)

    config = ConfigParser.ConfigParser()
    config.add('currency', currency, True)

    print currency + " added to config.ini"

def config_Load_Cur():
    with open('config.ini') as f:
        conf = f.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(conf))
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            whileloop = 1
            if each_val == 'True':
                while whileloop == 1:
                    try:
                        data = jsc.json_Import_Cur(each_key)
                        final = jsc.regex_Seperate(data)
                        dbc.database_Insert('cur_Mon', final[0], final[1], final[2], final[3])
                        print Fore.GREEN + "-------------------------------------------------------------------------------------------"
                        print Back.WHITE + Style.DIM + Fore.CYAN  + final[0] + Style.NORMAL + Fore.YELLOW + final[1]  + Fore.MAGENTA + Back.WHITE + final[2] + Fore.RED + Back.WHITE + final[3] + Fore.BLUE + Back.WHITE +" inserted into database" + Style.RESET_ALL
                        time.sleep(1)
                        whileloop = 0
                    except (IOError, TypeError, KeyError):
                        print Fore.RED + "WebAPI Timed out, Retrying"
                        time.sleep(3)
            else:
                print "config_Load_Cur failed"
