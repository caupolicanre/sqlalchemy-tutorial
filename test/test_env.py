import os
from os.path import dirname, join

import dotenv


dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)


message = os.environ.get('MESSAGE', None)
test = os.environ.get('TEST', None)

print(f'Message: {message}')
print(f'Test: {test}')