import json
import io
import time
import re


#Each api key is assigned a number and when this function is called the specific
#number given in parameters is called, if that number isn't on cooldown, it will
#be returned, otherwise the function will at +1 to that and find another key
def new_Key_Pull(number):
    data = """{
    "api1":{
    "api1": "Num 1",
    "cooldown": "True"
    },
    "api2":{
    "api2": "Num 2",
    "cooldown": "False"
    },
    "api3":{
    "api3": "Num 3",
    "cooldown": "True"
    }
    } """
    dat = json.loads(data)
    js = json.dumps(dat['api' + number])
    print(js)
    cooldown = re.search(r'{"cooldown": "(.*?), "api' + number + '(.*?)"}', js, )
    print (cooldown.group())



#This function sets the current state of an API key to false, and then waits for 62 seconds
#and resetts it to true in order to create a cooldown on each key so that api timeouts
#don't occurr
def cooldown_Key(api):
    conf = open('api_Keys.ini', w)
    config = ConfigParser.ConfigParser()

    config.set('API', api, 'False')
    time.sleep(62)
    config.set('API', api, 'True')
