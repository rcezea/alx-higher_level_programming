#!/usr/bin/python3
"""
Write a script that lists all states with a name\
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    state = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name LIKE %s", (state,))
    arr = []
    for row in cur.fetchall():
        arr.append(row[0])
    print(", ".join(arr))
