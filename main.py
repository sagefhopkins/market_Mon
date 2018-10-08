import importlib
import database_Controller as database
import json_Controller as jsc
import config_Controller_Rebuild as config
import interface_Controller as ic
import ConfigParser
import io
#import config_Controller as config

#database.database_Read('gear', 'B')

#API key GPR3TT0J4AM2EBBQ
#database.database_Table('ILS')
ic.main()

#with open('config.ini') as f:
#    conf = f.read()
#    config = ConfigParser.RawConfigParser(allow_no_value=True)
#    config.readfp(io.BytesIO(conf))
#    for (each_key, each_val) in config.items('currency'):
#        database.database_Table(each_key)
#jsc.json_Interpret_Cur("ILS")
#database.database_Table('cur_Mon')
#config.config_Load_Cur()

#database.database_Read('cur_Mon', 'ILS')

# Table Desc
#Curency,Currency Ticker, Exchange Rate , Open, High, Low, Close,
#Monitor, Date
