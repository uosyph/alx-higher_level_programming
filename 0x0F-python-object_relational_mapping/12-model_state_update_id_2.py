#!/usr/bin/python3
"""Changes the name of a State where id=2"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State).filter(State.id == 2)
    for row in result:
        row.name = 'New Mexico'
    session.commit()
    session.close()
