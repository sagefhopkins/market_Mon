import urllib as url
import json
import re
import io
from colorama import init, Fore, Style, Back

#Imports JSON data from web API, and returns data
def json_Import_Cur(currency):
    try:
        api = "http://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=" + currency + "&apikey=GPR3TT0J4AM2EBBQ"
        response = url.urlopen(api)
        data = json.loads(response.read())
    except IOError:
        print "Issue encountered on json_Import_Cur"

    return data
def regex_Seperate(data):
    try:
        var = json.dumps(data['Realtime Currency Exchange Rate'])
        final = []

        rl1 = re.search(r'("3.(.*?),)', var, )
        rl2 = re.search(r'("4.(.*?),)', var, )
        rl3 = re.search(r'("5.(.*?),)', var, )
        rl4 = re.search(r'("6.(.*?),)', var, )

        if rl1:
            ob1 = rl1.group()
            ss1 = re.search(r'(:(.*?)"(.*?)")', ob1, )
            if ss1:
                so1 = ss1.group()
                fl1 = (re.sub(':|"', '', so1))
                final.insert(1, fl1)
            else:
                print "ss1 has returned false"
            if rl2:
                ob2 = rl2.group()
                ss2 = re.search(r'(:(.*?)"(.*?)")', ob2, )
                if ss2:
                    so2 = ss2.group()
                    fl2 = (re.sub(':|"', '', so2))
                    final.insert(2, fl2)
                else:
                    print "ss2 has returned false"
                if rl3:
                    ob3 = rl3.group()
                    ss3 = re.search(r'(:(.*?)"(.*?)")', ob3, )
                    if ss3:
                        so3 = ss3.group()
                        fl3 = (re.sub(':|"', '' , so3))
                        final.insert(3, fl3)
                    else:
                        print "ss3 has returned false"
                    if rl4:
                        ob4 = rl4.group()
                        ss4 = re.search(r'(:(.*?)"(.*?)")', ob4, )
                        if ss4:
                            so4 = ss4.group()
                            fl4 = (re.sub(':|"', '', so4))
                            final.insert(4, fl4)
                            return final
                        else:
                            print"ss4 has returned false"
                    else:
                        print "rl4 has returned false"
                else:
                    print "rl3 has returned false"
            else:
                print "rl2 returned false"
        else:
            print "rl1 returned false"
    except(KeyError, TypeError):
        print Fore.RED + "-------------------------------------------------------------------------------------------"
        print Fore.RED + "Error Encountered"
        pass
