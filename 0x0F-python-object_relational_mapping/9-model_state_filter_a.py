#!/usr/bin/python3
"""
Write a script that prints the first State object
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]

    # Create engine connection
    engine = create_engine(f"mysql+mysqldb://{user}:{pw}@localhost:3306/{db}")
    conn = engine.connect()

    # Create a session for the connection
    Session = sessionmaker(engine)
    session = Session()

    # Query the database
    query = session.query(State).filter(State.name.like("%a%"))
    for row in query:
        print(f"{row.id}: {row.name}")
