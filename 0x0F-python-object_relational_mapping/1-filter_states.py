#!/usr/bin/python3

import MySQLdb
from MySQLdb import *
from sys import argv

def main():
    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()