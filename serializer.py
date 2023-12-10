import BienImmo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
from bson.json_util import dumps
import json 

# Name of the MongoDB collection to use 
collectionName = "biens"

# Initialize connection.
# Uses st.cache_resource to only run once.
#@st.cache_resource
def init_connection():
    # Create a new client and connect to the server
    mongo_uri=st.secrets["mongo"]["uri"]
    mongo_client = MongoClient(mongo_uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        mongo_client.admin.command('ping')
        print("successfully connected to MongoDB!")
        return mongo_client
    except Exception as e:
        print(e)
        return None

mongo_client = init_connection()
print(f"Mongo Client {mongo_client}")

def reset_connection():
    mongo_client = init_connection()

# Sauvegarder le bien dans une remote collection
def enregistrer_bien(bien):
    if mongo_client == None:
        raise Exception("MongoDB connection not initialized")
    db = mongo_client.client[st.secrets["mongo"]["db"]]
    collection = db[collectionName]
    result = collection.insert_one(bien.to_dict())
    print(result.inserted_id)
    return result.inserted_id

# Charger une liste de biens depuis une collection remote
# TODO Add support for pagination
def charger_liste_biens(limit):    
    print("Loading Properties from Remote MongoDB Collection")
    db = mongo_client.client[st.secrets["mongo"]["db"]]
    collection = db[collectionName]
    cursor = collection.find({}, {"_id": 0}).sort("_id", -1).limit(limit)
    liste_biens = []
    for doc in cursor:
        bienImmo = BienImmo.Bien(doc)
        liste_biens.append(bienImmo.to_summary())
    return liste_biens
    