#!/usr/bin/python3

import MySQLdb
from sys import argv


def main():
    print(argv[2])

    passw = "'" + argv[2] + "'"
    print(passw)
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=eval(passw), db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
