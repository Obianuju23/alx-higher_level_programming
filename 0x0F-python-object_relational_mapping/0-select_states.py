#!/usr/bin/python3
"""A python script to lists  all states from the database"""

if _name_ == '_main_':
    import MySQLdb
    import sys

    connect = MySQLdb.connect(host="localhost", port=3306,\
                              user=sys.argv[1], password=sys.argv[2],\
                              database=sys.argv[3])
    cursor = connect.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN\
            states ON cities.state_id = states.id ORDER BY cities.id ASC;"

    cursor.execute(sql)
    result = cursor.fetchall()
    for item in result:
        print(item)
    cursor.close()
    connect.close()
