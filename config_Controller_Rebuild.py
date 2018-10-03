import ConfigParser
import io
import json_Controller as jsc
import database_Controller as dbc
import time
from colorama import init, Fore, Back, Style
import threading
import re
import api_Key_Update as aku
import json
from sys import stdout

#Function used to add new currency tickers into config.ini
def config_Add_Cur(currency):
    conf = open('config.ini', w)
    config = ConfigParser.ConfigParser()
    config.add('currency', currency, True)
    print (currency + 'added to config.ini')

#Function used to load all currency data from config.ini and to pull current
#Market data related to the relative tickers
def config_Load_Cur():
    var = 0
    api_Key_Number = 1
    api_Key = ''
    arr = []
    whilel = 1

    Array = aku.new_Key_Pull(str(api_Key_Number))
    print Array

    with open('config.ini') as f:
        conf = f.read()
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(conf))
        while whilel == 1:
            if Array[0] != 'False':
                for (each_key, each_val) in config.items('currency'):
                    if var != 5:
                        try:
                            api = Array[1]
                            currency = each_key
                            data = jsc.json_Import_Cur(currency, api)
                            print(data)
                            print('-----------')
                            arr.insert(0, data['Realtime Currency Exchange Rate']['3. To_Currency Code'])
                            arr.insert(1, data['Realtime Currency Exchange Rate']['4. To_Currency Name'])
                            arr.insert(2, data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
                            arr.insert(3, data['Realtime Currency Exchange Rate']['6. Last Refreshed'])
                            print(arr)
                            dbc.database_Insert(arr[0], arr[0], arr[1], arr[2], arr[3])
                            print (Fore.GREEN + "-------------------------------------------------------------------------------------------")
                            print (Back.WHITE + Style.DIM + Fore.CYAN  + arr[0] + Style.NORMAL + Fore.YELLOW + arr[1]  + Fore.MAGENTA + Back.WHITE + arr[2] + Fore.RED + Back.WHITE + arr[3] + Fore.BLUE + Back.WHITE +" inserted into database" + Style.RESET_ALL)
                            var = var + 1
                            print var
                        except(KeyError):
                            pass
                    else:
                        print("Pulling New API Key")
                        aku.cooldown_Key(api_Key_Number, "False")

            else:
                if api_Key_Number != 3:
                    while Array[0] != "True":
                        api_Key_Number = api_Key_Number + 1
                        Array = aku.new_Key_Pull(str(api_Key_Number))
                        print(Array)
                else:
                    api_Key_Number = 1
