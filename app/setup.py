import pymongo
import os
from hashlib import sha256
import dotenv

dotenv = dotenv.load_dotenv(dotenv_path='.env')
db_host = os.environ.get('DB_HOST', 'localhost')
db_port = int(os.environ.get('DB_PORT', 27017))
db_name = os.environ.get('DB_NAME', 'test')
db_collection = os.environ.get('DB_COLLECTION', 'test')
admin_username = os.getenv('ADMIN_USER')
admin_password = os.getenv('ADMIN_PASSWORD').encode('utf-8')

print('Setting up database...')
print('Note that this will drop the database if it already exists.')
print('This will also create the admin user.')

conn = pymongo.MongoClient(db_host, db_port)
if db_name in conn.list_database_names():
    print('Dropping database...')
    conn.drop_database(db_name)

print('Creating database...')
db = conn[db_name]

print('Creating collection...')
collection = db[db_collection]

print('Creating admin user...')
collection.insert_one({'username': admin_username, 'password': sha256(admin_password).hexdigest(), 'role': 'admin'})
