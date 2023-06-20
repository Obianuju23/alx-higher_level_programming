#!/usr/bin/python3
"""
This is a script that imports the system args for command line, Mysqldb
module, connects to the database and then list out all the cities in the DB
"""

    import MySQLdb
    from sys import argv as sysarg
 if __name__ == '__main__':
   """Do not execute code when imported"""

    connector = MySQLdb.connect(host="localhost", port=3306, user=sysarg[1],
                              password=sysarg[2], database=sysarg[3])

    cursor = connector.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM states
               JOIN cities
               WHERE states.id = cities.state_id
               ORDER BY cities.id"""

    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    connector.close()
