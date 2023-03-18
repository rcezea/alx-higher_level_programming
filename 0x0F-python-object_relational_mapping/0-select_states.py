#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    db = db.cursor()
    db.execute("SELECT * FROM states ORDER BY id")
    [print (row) for row in db.fetchall()]