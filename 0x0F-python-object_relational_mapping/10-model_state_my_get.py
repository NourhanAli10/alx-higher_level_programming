#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state name>"
            .format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2],
            sys.argv[3], sys.argv[4]),
        pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State table for the given state name
    result = session.query(State).filter(State.name == state_name).first()

    # Check if the state was found or not
    if result:
        print(result.id)
    else:
        print("Not found")

    # Close the session
    session.close()
