#!/usr/bin/python3
"""Adds a new State object 'Louisiana'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[1]}',
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    session.add(State(name='Louisiana'))
    session.commit()
    print(session.query(State).filter(State.name == 'Louisiana')[0].id)
    session.close()
