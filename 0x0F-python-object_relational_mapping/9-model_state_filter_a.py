#!/usr/bin/python3
"""Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py <mysql username> /
                                   <mysql password> /
                                   <database name>"""

from sys import argv as sysarg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """This does not execute if imported"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sysargv[1], sysargv[2], sysargv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{:d}: {:s}".format(state.id, state.name))
    session.close()
