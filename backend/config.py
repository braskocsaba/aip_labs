import os

DB_HOST_TEST = os.environ.get('DB_HOST_TEST', 'localhost')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'aip_labs')
DB_USER = os.environ.get('DB_USER', 'local_user')
DB_PASS = os.environ.get('DB_PASS', 'pwd12345')
