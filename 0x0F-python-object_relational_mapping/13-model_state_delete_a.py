#!/usr/bin/python3
"""Deletes the State object that contains 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State).all()
    for row in result:
        if 'a' in str(row):
            session.delete(row)
    session.commit()
    session.close()
