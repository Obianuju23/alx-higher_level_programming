#!/usr/bin/python3
"""
A script that deletes all State objects with a name
containing the letter a from the database
hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv as sysarg


if __name__ == "__main__":
    """so if imported does not excute"""

    engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                           format(sysarg[1], sysarg[2], sysarg[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%"))
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
