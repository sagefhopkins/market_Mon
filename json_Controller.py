import urllib as url
import json
import re
import io
from colorama import init, Fore, Style, Back
import time

#Imports JSON data from web API, and returns data
def json_Import_Cur(currency, api):
    whileloop = 1
    while whileloop == 1:
        try:
            url_Api = "http://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=" + str(currency) + "&apikey=" + str(api)
            print(url_Api)
            response = url.urlopen(url_Api)
            data = json.loads(response.read())
            whileloop = 0
            return data
        except IOError:
            print "Issue encountered on json_Import_Cur"
            time.sleep(20)
        except ValueError:
            print api
            print response
            time.sleep(20)
