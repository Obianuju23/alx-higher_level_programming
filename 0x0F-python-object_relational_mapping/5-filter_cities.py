#!/usr/bin/python3
"""This is a script that imports the system args for command line, Mysqldb
module, connects to the database and then list out all the cities in the DB
"""

if __name__ == '__main__':
    import MySQLdb as mysql
    from sys import argv as sysarg

    """Connects to the database"""
    connector = mysql.connect(host='localhost', port=3306, user=sysarg[1],
                              password=sysarg[2], database=sysarg[3])
    data = (sysarg[4],)
    cursor = connector.cursor()
    query = "SELECT `cities`.`name` AS `cname` FROM `cities` INNER JOIN\
            `states` ON `cities`.`state_id` = `states`.`id` WHERE\
            `states`.`name` = %s ORDER BY `cities`.`id` ASC;"
    cursor.execute(query, data)
    results = cursor.fetchall()
    print(", ".join([item[0] for item in results]))
    cursor.close()
    connector.close()
