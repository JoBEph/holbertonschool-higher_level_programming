#!/usr/bin/python3
""" Safe filters states
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
        port=3306,
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
