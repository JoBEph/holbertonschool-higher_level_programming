#!/usr/bin/python3
"""
filter states by user input
"""
import MySQLdb
import sys

if __name__ == "__main__":
    def filter_states():
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        db = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            db=database,
            charset="utf8",
            port=3306
            )
        cursor = db.cursor()
        query = (
            "SELECT * FROM states "
            "WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
        )
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
    filter_states()
