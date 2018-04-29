from pymongo import MongoClient 
import pandas as pd

client = MongoClient()
client = MongoClient("mongodb://localhost:27017")
client.database_names()
db = client.tanonbase
db.collection_names()
collection = db.tanon_collection
collection.find_one()

df = pd.read_csv("./ks-projects-201801-sample.csv") #on charge le fichier csv
objects = df.to_json(orient="records") #On transforme les éléments contenu dans le fichier en objets
collection.insert_many(objects)

#recupérer les 5 projets ayant reçu le plus de promesses de dons

collection.find().sort("pledged",-1).limit(5)



