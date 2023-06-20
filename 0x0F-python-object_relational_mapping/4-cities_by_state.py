#!/usr/bin/python3
"""This is a script that imports the system args for command line, Mysqldb
module, connects to the database and then list out all the cities in the DB
"""

    import MySQLdb
    from sys import argv as sysarg
 if __name__ == '__main__':
   """Do not execute code when imported"""

    connector = MySQLdb.connect(host='localhost', port=3306, user=sysarg[1],
                              password=sysarg[2], database=sysarg[3])

    cursor = connector.cursor()
    query = "SELECT `cities`.`id` AS `cid`, `cities`.`name` AS `cname`,\
            `states`.`name` AS `sname` FROM `cities` INNER JOIN `states`\
            ON `cities`.`state_id` = `states`.`id` ORDER BY\
            `cities`.`id` ASC;"
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    connector.close()
