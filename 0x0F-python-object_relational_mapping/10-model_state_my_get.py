#!/usr/bin/python3
"""Prints the State object with the name passed as an argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[1]}',
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = [row.id for row in session.query(State).
              filter(State.name == sys.argv[4])]
    if result:
        for e in result:
            print(e)
    else:
        print("Not found")
    session.close()
