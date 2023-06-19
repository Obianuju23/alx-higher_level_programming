#!/usr/bin/python3
"""A python script to lists  all states from the database"""

if _name_ == '_main_': 
    """This means that all the code inside this block will not be executed if imported"""
    import MySQLdb
    from sys  import argv as sysarg

    connect = MySQLdb.connect(host="localhost",
                              port=3306, user=sysargv[1],
                              password=sysargv[2],
                              database=sysargv[3])
    cursor = connect.cursor()
    query  = "SELECT * FROM states ORDER id ASC;"

    cursor.execute(query)
    result = cursor.fetchall()
    for item in result:
        print(item)
    cursor.close()
    connect.close()
