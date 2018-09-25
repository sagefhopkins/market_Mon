import ConfigParser
import io
import json_Controller as jsc
import database_Controller as dbc
import time


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
            whileloop = 1
            if each_val == 'True':
                while (whileloop = 1)
                    try:
                        data = jsc.json_Import_Cur(each_key)
                        final = jsc.regex_Seperate(data)
                        dbc.database_Insert('cur_Mon', final[0], final[1], final[2], final[3])
                        print final[0] + final[1] + final[2] + final[3] + " inserted into database"
                        print "Wating a few seconds"
                        time.sleep(5)
                        print "Done sleeping!"
                        whileloop = 0
                    except (IOError, TypeError, KeyError):
                        print "Error encountered moving on"
                        time.sleep(15)
            else:
                print "config_Load_Cur failed"
