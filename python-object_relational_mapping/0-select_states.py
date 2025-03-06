#!/usr/bin/env python3
""" Module to list all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    def get_states():
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cursor.fetchall()

        for row in states:
            print(row)
        cursor.close()
        db.close()

    get_states()
