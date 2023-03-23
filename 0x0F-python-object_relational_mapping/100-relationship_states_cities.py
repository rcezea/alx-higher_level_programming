#!/usr/bin/python3
'''
script that creates the State
“California” with the City “San
Francisco” from the database hbtn_0e_100_usa
'''

from sys import argv
from relationship_city import City, Base, eng
from sqlalchemy.orm import Session
from relationship_state import State
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(f"mysql+mysqldb:\
                           //{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    session = Session
    s1 = State(name='California')
    c1 = City(name='San Francisco')
    s1.cities.append(c1)
    session.add_all([s1, c1])
    session.commit()
