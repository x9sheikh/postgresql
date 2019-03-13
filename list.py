import os

import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

engine = create_engine(os.getenv("postgresql://x9sheikh:@X9sheikh.usama@localhost:5432/flights"))
# IN postgres my usename='x9sheikh' & password='@X9sheikh.usama'. SO, I did it in above statement


db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(flight)

if __name__ == "__main__":
    main()