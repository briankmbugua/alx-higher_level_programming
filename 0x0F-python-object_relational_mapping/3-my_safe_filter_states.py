#!/usr/bin/python3

"""
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.

Script is also safe from MYSQL injections
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
            ORDER BY states.id", (sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
