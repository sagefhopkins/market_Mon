import sqlite3

#Initializes database connection and returns connection to function caller
def database_Connect():
    connection = sqlite3.connect('cur_Monitor.db')

    return connection

#Inserts new rows into a table, this is created to ensure uniformity between rows
def database_Insert(table, ticker, currency, exchange, open, high, low, close, montior, date ):
    sql = database_Connect()
    query = "INSERT INTO " + table + " VALUES('" + ticker + "', '" + currency + "', '" + exchange + "', '" + open + "', '" + high + "', '" + low + "', '" + close + "', '" + monitor + "', '" + date + "')"
    sql.execute(query)
    sql.commit()
    print (query + "Entered into database!")

#Queries the table, and returns all values which either match or include the
#name string in their overall value
def database_Read(table, currency):
    sql = database_Connect()
    query = "SELECT * FROM " + table + " WHERE currency LIKE '" + currency + "%'"
    for row in sql.execute(query):
        print row

#Creates new tables into the database, this will always use the same format
#to ensure uniformity between tables
def database_Table(name):
    sql = database_Connect()
    query = "CREATE TABLE " + name + " (currency text, exchange int, open int, high int, low int, close int, monitor int, date timestamp)"
    sql.execute(query)
    sql.commit()
    print name + " New table created!"

#Allows the ordering of table read outs to help allow users to view data better
def database_Order(table, order):
    sql = database_Connect()
    query = "SELECT * FROM " + table + " ORDER BY " + order
    for row in sql.execute(query):
        print row
