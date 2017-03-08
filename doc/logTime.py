import datetime
import sqlite3

sqlite_file = 'logTime.db' #saves the database file
now = datetime.datetime.now() #creates the date and time
conn = sqlite3.connect(sqlite_file) #creates connection to db file
c = conn.cursor() #creates way to alter conn
def logTime():
  c.execute("INSERT INTO DateTime values(DATE('now'), TIME('now'))") #inserts into respective colums
  conn.commit()
  conn.close()
logTime()

