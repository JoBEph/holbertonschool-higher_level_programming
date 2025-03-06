#!/usr/bin/env python3
""" Module to list all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
        rows = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8",
            port=3306
        )
        cursor = rows.cursor()
        cursor.execute("SELECT * FROM states ORDER BY ASC")
        states = cursor.fetchall()

        for row in states:
            print(row)
        cursor.close()
        rows.close()
