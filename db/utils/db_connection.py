import os
from os.path import dirname, join

import dotenv

from sqlalchemy import create_engine



dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

db_url = os.environ.get('DATABASE_URL')
db_name = os.environ.get('DATABASE_NAME')
db_user = os.environ.get('DATABASE_USER')
db_password = os.environ.get('DATABASE_PASSWORD')


def get_db_connection():
    '''
    Function to get the database connection.

    Returns
    -------
    sqlalchemy.engine.base.Connection
        Database connection.
    '''
    return create_engine(f'mysql+mysqlconnector://{db_user}@{db_url}/{db_name}')