from sqlalchemy.orm import Session

from app.models import User, Address

from db.funcs.db_connection import get_db_connection



engine = get_db_connection()



def get_all_users():
    with Session(engine) as session:
        users = session.query(User).all()
        for user in users:
            print(user)


def find_user_by_username(username: str):
    with Session(engine) as session:
        user = session.query(User).filter_by(username=username).first()
        if user:
            print(f"User found: {user}")
        else:
            print(f"User with username {username} not found.")


def update_user_fullname(user_id: int, new_fullname: str):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            user.fullname = new_fullname
            session.commit()
            print(f"User {user.username}'s fullname updated to {new_fullname}.")
        else:
            print(f"User with id {user_id} not found.")


def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            print(f"User {user.username} deleted.")
        else:
            print(f"User with id {user_id} not found.")



if __name__ == "__main__":

    print('\nGet all users.')
    get_all_users()

    print('\nFind a user by username.')
    find_user_by_username(input(f'\nEnter the username to search: '))

    print('\nUpdate the fullname of an user.')
    update_user_fullname(int(input('User ID: ')), input('New fullname: '))

    print('\nDelete an user.')
    delete_user(int(input('\nEnter the ID of the user to delete: ')))