#!/usr/bin/python3
"""
List all states from hbtn_0e_0_usa
    """
import MySQLdb
import sys


if __name__ == "__main__":
    def list_states():
        """ Lists all states from the database hbtn_0e_0_usa
        """

        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            charset="utf8",
            port=3306
            )
        cur = db.cursor()

        cur.execute('SELECT * FROM states ORDER BY id ASC')

        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        db.close()

    list_states()
