#!/usr/bin/python3

"""
Script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name\
            FROM cities RIGHT JOIN states ON\
            state_id = states.id WHERE states.name='{}'\
            ORDER BY cities.id".format(sys.argv[4], ))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        if i + 1 == len(rows):
            print(row[0])
        print(row[0], end=", ")
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
