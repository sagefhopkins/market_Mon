import importlib
import database_Controller as database
import json_Controller as jsc
import config_Controller_Threading as config
#import config_Controller as config

#database.database_Read('gear', 'B')

#API key GPR3TT0J4AM2EBBQ


#jsc.json_Interpret_Cur("ILS")
#database.database_Table('cur_Mon')
config.config_Load_Cur()

database.database_Read('cur_Mon', 'ILS')

# Table Desc
#Curency,Currency Ticker, Exchange Rate , Open, High, Low, Close,
#Monitor, Date
