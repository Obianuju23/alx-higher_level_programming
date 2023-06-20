#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql username> /
                                    <mysql password> /
                                    <database name>
"""
from sys import argv as sysarg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """This does not execute if imported"""

    engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                           format(sysarg[1], sysarg[2], sysarg[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(instance.id, instance.name))
    session.close()
