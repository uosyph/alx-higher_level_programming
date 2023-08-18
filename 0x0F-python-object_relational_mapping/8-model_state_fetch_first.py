#!/usr/bin/python3
"""Prints the first State object from database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State).first()
    print(result) if result else print("Nothing")
    session.close()
