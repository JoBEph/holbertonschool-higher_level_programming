#!/usr/bin/python3
"""a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    def filter_list():

        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            charset="utf8",
            port=3306
            )
        cur = db.cursor()
        cur.execute("SELECT * FROM states \
                WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
        states = cur.fetchall()
        for row in states:
            print(row)
        cur.close()
        db.close()
    filter_list()
