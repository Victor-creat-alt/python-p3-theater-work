#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Role, Audition
import ipdb

def main():
    engine = create_engine('sqlite:///theater.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Sample data
    roles = [
        Role(character_name="Andrew"),
        Role(character_name="Jennifer"),
        Role(character_name="Mark")
    ]

    auditions = [
        Audition(actor="James Deen", location="Stockholm", phone_number="1234567890", hired=False, role_id=1),
        Audition(actor="Judas Simon", location="Tashkent", phone_number="0987654321", hired=True, role_id=2)
    ]

    # Add data to session and commit
    session.add_all(roles)
    session.add_all(auditions)
    session.commit()

    print("Database seeded successfully!")

    # Enter ipdb shell
    ipdb.set_trace()

if __name__ == "__main__":
    main()
