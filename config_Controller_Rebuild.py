import ConfigParser
import io
import json_Controller as jsc
import database_Controller as dbc
import time
from colorama import init, Fore, Back, Style
import threading
import re
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
    api_Key = '967OAAEVKJ9WT8F1'
    arr = []
    whilel = 1
    var = 1

    with open('config.ini') as f:
        conf = f.read()
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(conf))
        while whilel == 1:
            for (each_key, each_val) in config.items('currency'):
                try:
                    currency = each_key
                    data = jsc.json_Import_Cur(currency, api_Key)
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
                    if var == 4:
                        print("-------------------------------------------------------------------------------------------")
                        print ("Sleeping 60 Seconds")
                        time.sleep(60)
                        var = 1
                    else:
                        var = var + 1

                except(KeyError):
                    pass
