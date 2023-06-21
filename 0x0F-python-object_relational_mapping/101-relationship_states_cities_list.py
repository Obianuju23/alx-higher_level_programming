#!/usr/bin/python3

"""A python script that lists all states and the corresponding cities
owned by that state in the DB using SQLAlchemy ORM"""

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

    Session = sessionmaker(bind=engine)
    session = Session()

    listall = session.query(State).outerjoin(City).order_by(State.id,
                                                            City.id).all()
    for state in listall:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
    connection.close()
