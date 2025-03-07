#!/usr/bin/python3
""" Models state fetch all"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True,)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]
    state = (session.query(State)
             .filter_by(name=state_name).order_by(State.id).first())

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
