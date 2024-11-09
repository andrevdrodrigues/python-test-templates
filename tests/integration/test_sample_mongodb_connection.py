
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pytest

def test_mongodb_connection_successful():
   connected = True

   try:
      client = MongoClient(host = ["localhost:1111"], serverSelectionTimeoutMS = 2000) # it fails, is necessary to add a valid host url
   except ConnectionFailure:
      connected = False

   assert connected is False

