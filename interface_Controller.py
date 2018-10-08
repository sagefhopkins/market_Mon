from __future__ import division
import sys
import os
import time
import database_Controller as dbc
from clint.textui import prompt, puts, colored, validators, progress, indent
import config_Controller_Rebuild as ccr



def main():
    options = [
    {'selector':'1', 'prompt':'Pull Data', 'return': 'Pull Data'},
    {'selector':'2', 'prompt':'View Data', 'return': 'View Data'},
    {'selector':'3', 'prompt':'Edit Config', 'return': 'Edit Config'}
              ]
    opt_1 = prompt.options('Select What You Would Like to Do From The List Below:', options)

    puts(colored.red('Option {0} selected').format(opt_1))

    if opt_1 == 'Pull Data':
        print(chr(27) + '[2J')
        options = [
            {'selector':'1', 'prompt':'Currency Data', 'return': 'Currency Data'},
            {'selector':'2', 'prompt':'Stock Data', 'return': 'Stock Data'},
            {'selector':'3', 'prompt':'Crypto Data', 'return': 'Crypto Data'}
                  ]
        opt_1_1 = prompt.options('Select Which Type of Data You\'d like to pull:', options)
        if opt_1_1 == 'Currency Data':
            print(chr(27) + '[2J')
            puts(colored.green('This will take approximately ' + str(156*60/60) + 'minutes!'))
            ccr.config_Load_Cur()
            puts(colored.green('Data Pull Completed!'))
            time.sleep(5)
            main()
        elif opt_1_1 == 'Stock Data':
            puts(colored.red('This feature is not yet completed! Please try again in a different version!'))
            time.sleep(2)
            print(chr(27) + '[2J')
            main()
        elif opt_1_1 == 'Crypto Data':
            puts(colored.red('This feature is not yet completed! Please try again in a different version!'))
            time.sleep(2)
            print(chr(27) + '[2J')
            main()

    elif opt_1 == 'View Data':
        print(chr(27) + '[2J')
        options = [
            {'selector':'1', 'prompt':'Currency Data', 'return': 'Currency Data'},
            {'selector':'2', 'prompt':'Stock Data', 'return': 'Stock Data'},
            {'selector':'3', 'prompt':'Crypto Data', 'return': 'Crypto Data'}
                  ]
        opt_1_2 = prompt.options('Select Which Type of Data You\'d Like to Pull:', options)
        if opt_1_2 == 'Currency Data':
            print(chr(27) + '[2J')
            currency = prompt.query('Which Currency Would You Like to Pull Data From(Ticker)?:')
            sql = dbc.database_Connect()
            query = ("SELECT * FROM {0}").format(currency)
            i = 0
            with indent(4, quote='%%%%'):
                for row in sql.execute(query):
                    puts(colored.white(str(row)))
            options = [
                {'selector':'1', 'prompt':'Plot Data', 'return': 'Plot Data'},
                {'selector':'2', 'prompt':'Show Total Change', 'return': 'Show Total Change'},
                {'selector':'3', 'prompt':'Return Home', 'return': 'Return Home'}
                ]
            opt_1_2_1 = prompt.options('What Would You Like to Do Next?:', options)
            if opt_1_2_1 == 'Plot Data':
                print('t')

            elif opt_1_2_1 == 'Show Total Change':
                query = "SELECT `exchange`, `date` FROM {0} ORDER BY `exchange` ASC".format(currency)
                cursor = sql.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                data_opt_1_2_1 = [list(i) for i in results]
                #print results
                change = map(lambda i: i[0], results)
                dates  = map(lambda x: x[1], results)

                puts('Minimum: {0}'.format(change[-1]))
                puts('Mindate: {0}'.format(time.ctime(dates[-1])))
                puts('Maximum: {0}'.format(change[0]))
                puts('Maxdate: {0}'.format(time.ctime(dates[0])))

                change = change[0] - change[-1]
                puts('Total change: ', newline=False) 
                if change > 0:
                    puts(colored.green('+{0}'.format(change)))
                else:
                    puts(colored.red(str(change)))

                #print (data_opt_1_2_1)

            elif opt_1_2_1 == 'Return Home':
                print(chr(27) + '[2J')
                main()

        elif opt_1_2 == 'Stock Data':
            puts(colored.red('This feature is not yet completed! Please try again in a different version!'))
            time.sleep(2)
            print(chr(27) + '[2J')
            main()
        elif opt_1_2 == 'Crypto Data':
            puts(colored.red('This feature is not yet completed! Please try again in a different version!'))
            time.sleep(2)
            print(chr(27) + '[2J')
            main()
    elif opt_1 == 'Edit Config':
        print(chr(27) + '[2J')
        print 'Edit Config selected'
