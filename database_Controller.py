import sqlite3

#Initializes database connection and returns connection to function caller
def database_Connect():
    connection = sqlite3.connect('cur_Monitor.db')

    return connection

#Inserts new rows into a table, this is created to ensure uniformity between rows
def database_Insert(table, ticker, currency, exchange, date ):
    try:
        sql = database_Connect()
        query = "INSERT INTO " + table + " VALUES('" + ticker + "', '" + currency + "', '" + exchange + "', '" + date + "')"
        sql.execute(query)
        sql.commit()
        print (query + "Entered into database!")
    except(TypeError, KeyError):
        pass
        print "Error occurred databasing!"

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
    query = "CREATE TABLE " + name + " (ticker text , currency text, exchange int, date text)"
    sql.execute(query)
    sql.commit()
    print name + " New table created!"

#Allows the ordering of table read outs to help allow users to view data better
def database_Order(table, order):
    sql = database_Connect()
    query = "SELECT * FROM " + table + " ORDER BY " + order
    for row in sql.execute(query):
        print row
