#!/usr/bin/python3

""" Changes the name of a State object from the database
hbtn_0e_6_usa by id 2 """

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

    update = session.query(State).filter(State.id == 2).first()
    if update:
        update.name = "New Mexico"
        session.commit()

    session.close()
