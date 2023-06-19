#!/usr/bin/python3
"""A python script to lists  all states from the database"""

import MySQLdb
from sys  import argv as sysarg

if __name__ == '__main__':
    """This means that all the code inside this block will not be executed if imported"""
    connector = MySQLdb.connect(host="localhost",
                              port=3306, user=sysarg[1],
                              password=sysarg[2],
                              database=sysarg[3])
    cursor = connector.cursor()
    query  = "SELECT * FROM states ORDER id ASC;"

    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    connector.close()
