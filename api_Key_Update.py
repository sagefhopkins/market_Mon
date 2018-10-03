import json
import io
import time
import re


def json_Data_Pull():
    data = open('api_Keys.json', 'r')
    print data

    return data

#Each api key is assigned a number and when this function is called the specific
#number given in parameters is called, if that number isn't on cooldown, it will
#be returned, otherwise the function will at +1 to that and find another key
def new_Key_Pull(number):
    data = json_Data_Pull()
    arr = []
    try:
        loads = json.loads(data)
        #js = json.dumps(loads['api' + number])
        #print (js)
        #cooldown = re.search(r'("cooldown": "(.*?)")', js, )
        #final = re.sub(r'"cooldown": "|"', '' , cooldown.group())
        #arr.insert(1, final)
        #api = re.search(r'("api(.*)": "(.*?)"})', js, )
        #final2 = re.sub(r'"api(.*)": "|"|}', '', api.group())
        #arr.insert(2, final2)
        cooldown = loads['api' + number]['cooldown']
        api = loads['api' + number]['api' + number]
        arr.insert(0, cooldown)
        arr.insert(1, api)

        return arr
    except(TypeError):
        pass

#This function sets the current state of an API key to false, and then waits for 62 seconds
#and resetts it to true in order to create a cooldown on each key so that api timeouts
#don't occurr
def cooldown_Key(api, cooldown):
    loads = json.loads(json_Data_Pull())
    loads[api]["cooldown"] = cooldown
