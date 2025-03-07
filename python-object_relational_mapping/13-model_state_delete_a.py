#!/usr/bin/env python3

""" Delete state with a """

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

    delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in delete:
        session.delete(state)
    session.commit()
    session.close()
