# db.py
from pymongo import MongoClient

# Define the MongoDB connection URI
MONGO_URI = 'mongodb://localhost:27017/'

try:
    # Attempt to connect to MongoDB
    client = MongoClient(MONGO_URI)
    print("MongoDB is running.")
    db = client['test_CK_DB']
except Exception as e:
    print("Failed to connect to MongoDB:", e)

# Get the database object
