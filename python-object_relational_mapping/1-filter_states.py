#!/usr/bin/python3
"""
filter states by user input
"""
import MySQLdb
import sys

if __name__ == "__main__":
        """def filter_states():"""

        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            charset="utf8",
            port=3306
            )

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states \
                WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()
