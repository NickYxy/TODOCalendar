__author__ = 'nickyuan'

from pymongo import *

# mongo config
db_name = 'todo_db'
client = MongoClient("mongodb://localhost:1111")
db = client[db_name]

# config
config_dict = dict(

)
