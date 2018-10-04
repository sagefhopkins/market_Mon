import json
import io
import time
import re


#Each api key is assigned a number and when this function is called the specific
#number given in parameters is called, if that number isn't on cooldown, it will
#be returned, otherwise the function will at +1 to that and find another key
def new_Key_Pull(number):
    with open('api_Keys.json') as f:
        data = json.load(f)
        print(number)
    arr = []
    try:
        cooldown = data['api' + number]['cooldown']
        api = data['api' + number]['api_Key']
        arr.insert(0, cooldown)
        arr.insert(1, api)

        return arr
    except(TypeError):
        pass

#This function sets the current state of an API key to false, and then waits for 62 seconds
#and resetts it to true in order to create a cooldown on each key so that api timeouts
#don't occurr
def cooldown_Key(api, cooldown):
    with open('api_Keys.json') as r:
        data = json.load(r)
        r.close()
    with open('api_Keys.json', 'w') as f:
        old_Cooldown = data['api' + str(api)]['cooldown']
        data['api' + str(api)]['cooldown'] = cooldown
        f.seek(0)
        json.dump(data, f)
        f.close()
