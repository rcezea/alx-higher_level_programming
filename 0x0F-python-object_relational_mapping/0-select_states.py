#!/usr/bin/python3

import MySQLdb
from sys import argv

def main():

    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id DESC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

if __name__ == '__main__':
    main()
