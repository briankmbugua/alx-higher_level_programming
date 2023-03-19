#!/usr/bin/python3
"""
Python module for listing all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
if __name__ == '__main__':
    """
    Only executable if run directly
    """
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Close all cursors    
    cursor.close()
    # Close all databases
    database.close()
