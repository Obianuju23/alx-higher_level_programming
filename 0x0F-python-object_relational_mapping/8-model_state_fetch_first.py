#!/usr/bin/python3
"""A script to list the first state in the DB using SQLAlchemy ORM"""

from sys import argv as sysarg
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

    First_State = session.query(State).order_by(State.id).first()
    if First_State is not None:
        print("{:d}: {:s}".format(First_State.id, First_State.name))
    else:
        print("Nothing")
    session.close()
