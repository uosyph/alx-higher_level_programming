#!/usr/bin/python3
"""Lists all State objects from the hbtn_0e_6_usa db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State, City).join(City)
    for row in result:
        print(f"{str(row[0]).split(':')[1][1:]}:{str(row[1]).split(':')[1]}")
    session.close()
