#!/usr/bin/python3
"""Links a class to a table in a database"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    city = City(name='San Francisco')
    state = State(name='California', cities=[city])
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
