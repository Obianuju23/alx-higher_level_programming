#!/usr/bin/python3
"""A script to list the first state in the DB using SQLAlchemy ORM"""

import sys import argv as sysarg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """This does not execute if imported"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    FirstState = session.query(State).order_by(State.id).first()
    if FirstState is None:
        print("Nothing")
    else:
        print("{:d}: {:s}".format(FirstState.id, FirstState.name))
    session.close()
