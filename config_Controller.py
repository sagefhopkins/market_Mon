import ConfigParser
import io
import json_Controller as jsc
import database_Controller as dbc


def config_Add_Cur(currency):
    conf = open('config.ini', w)

    config = ConfigParser.ConfigParser()
    config.add('currency', currency, True)

    print currency + " added to config.ini"

def config_Load_Cur():
    print "config_Load_Cur"
    with open('config.ini') as f:
        conf = f.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(conf))
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            print each_key
            print each_val
            if each_val == 'True':
                data = jsc.json_Import_Cur(each_key)
                final = jsc.regex_Seperate(data)
                dbc.database_Insert('cur_Mon', final[0], final[1], final[2], final[3])
                print final[0] + final[1] + final[2] + final[3] + " inserted into database"
            else:
                print "config_Load_Cur failed"
