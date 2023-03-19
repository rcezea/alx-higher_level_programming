#!/usr/bin/python3
"""
write a script 14-model_city_fetch_by_state.py
that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
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
    query = session.query(City, State).filter(State.id == City.state_id).all()

    for row in query:
        print(f"{row[1].name}: ({row[0].id}) {row[0].name}")
