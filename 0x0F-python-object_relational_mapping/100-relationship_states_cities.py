#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    new_state = State(name='California', cities=[City(name='San Francisco')])

    session.add(new_state)
    session.commit()

    session.close()
