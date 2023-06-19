#!/usr/bin/python3
"""A script that imports the system args for command line, Mysqldb
module, connects to the database and then list out all the states in the DB
that starts with the letter N
"""

if __name__ == '__main__':
    import MySQLdb as mysql
    from sys import argv as sysarg

    """Connects to the database"""
    connector = mysql.connect(host='localhost', port=3306, user=sysarg[1],
                              password=sysarg[2], database=sysarg[3])
    cursor = connector.cursor()
    query = "SELECT * FROM `states` WHERE `name` LIKE BINARY 'N%' ORDER \
            BY `id` ASC;"
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    connector.close()
