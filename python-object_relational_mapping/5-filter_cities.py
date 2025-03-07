#!/usr/bin/python3
""" cities by states"""

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
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],),)
    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
