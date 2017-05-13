import sqlite3 as db
import sys
import signal

con = db.connect('/ELProjmnt/envData.db')
cur = con.cursor()
cur.execute('SELECT SQLITE_VERSION()')
data = cur.fetchone()
print "SQLite version: %s" % data

import getData

loggedData = [0,0,0,0,0]
#line = cur.execute('''select max(rowid) from data''')

line = 1

def sigint_handler(signal, frame):
    print 'Interrupted: DB connection closing...'
    con.close()
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)




