from sqlalchemy.orm import Session
from faker import Faker

from app.models import User, Address

from db.funcs.db_connection import get_db_connection


engine = get_db_connection()

fake = Faker()


def populate_db(num_users: int, num_addresses_per_user: int):
    '''
    Populate the database with random users and addresses.

    Parameters
    ----------
    num_users : int
        Number of users to create.
    num_addresses_per_user : int
        Number of addresses to create for each user.
    '''
    with Session(engine) as session:
        for _ in range(num_users):
            user = User(
                username=fake.user_name(),
                fullname=fake.name(),
                age=fake.random_int(min=18, max=90)
            )
            session.add(user)
            session.commit()  # Commit the user to get the ID

            for _ in range(num_addresses_per_user):
                address = Address(
                    email_address=fake.email(),
                    user_id=user.id  # Associate the address with the user
                )
                session.add(address)

        session.commit()



if __name__ == "__main__":
    print('\nPopulate the database with random users and addresses.')

    num_users = int(input('Enter the number of users to create: '))
    num_addresses_per_user = int(input('Enter the number of addresses to create for each user: '))

    populate_db(num_users, num_addresses_per_user)
