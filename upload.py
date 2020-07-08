import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Checking For Environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is no set")

# Setting-up interface for interaction with database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    # loading data stored in the csv file
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights(origin, destination, duration) VALUES (:origin, :destination, :duration)",
                   {"origin": origin, "destination": destination, "duration": duration})
        print(f"Flight added from {origin} to {destination} lasting {duration} minutes")
    db.commit()


if __name__ == '__main__':
    main()
