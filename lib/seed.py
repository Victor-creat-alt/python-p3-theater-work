#!/usr/bin/env python3

from faker import Faker # type: ignore
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Role, Audition

if __name__ == '__main__':
    engine = create_engine('sqlite:///theater.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Role).delete()
    session.query(Audition).delete()
    
    fake = Faker()

    # Sample data generation
    roles = [
        Role(character_name="Andrew"),
        Role(character_name="Jennifer"),
        Role(character_name="Mark")
    ]

    auditions = []
    for role in roles:
        session.add(role)
        session.commit()

        for _ in range(random.randint(1, 5)):
            audition = Audition(
                actor=fake.name(),
                location=fake.city(),
                phone_number=fake.phone_number(),
                hired=random.choice([True, False]),
                role_id=role.id
            )
            auditions.append(audition)
    
    session.bulk_save_objects(auditions)
    session.commit()
    session.close()

    print("Database seeded successfully!")
