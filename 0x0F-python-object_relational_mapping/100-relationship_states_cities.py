#!/usr/bin/python3

"""A python script that creates a State with a City form the DB using
SQLAlchemy ORM
"""

from sys import argv as sysarg
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=sysarg[1], password=sysarg[2],
                                 database=sysarg[3])

    engine = create_engine('mysql+mysqldb://', creator=lambda: connection,
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add_all([new_state, new_city])
    session.commit()

    session.close()
    connection.close()
