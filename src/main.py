import sqlite3
 
con = sqlite3.connect('publications.db')
cur = con.cursor()




con.close()