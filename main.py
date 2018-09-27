import importlib
import database_Controller as database
import json_Controller as jsc
#import config_Controller_Threading as config
import ConfigParser
import io
#import config_Controller as config

#database.database_Read('gear', 'B')

#API key GPR3TT0J4AM2EBBQ


#jsc.json_Interpret_Cur("ILS")
#database.database_Table('cur_Mon')
#config.config_Load_Cur()

with open('config.ini') as f:
    conf = f.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(conf))
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
                database.database_Table(each_key)
                time.sleep(1)

# Table Desc
#Curency,Currency Ticker, Exchange Rate , Open, High, Low, Close,
#Monitor, Date
