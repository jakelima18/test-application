"""This module is to configure app to connect with database."""

from pymongo import MongoClient

DATABASE = MongoClient()['restfulapi'] # DB_NAME
DEBUG = True
client = MongoClient('mongo', 27017)
