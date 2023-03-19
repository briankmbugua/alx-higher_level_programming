#!/usr/bin/python3

"""
Module that contains a script that lists
all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
conn = engine.connect()
conn.execute("SELECT * State.__table
