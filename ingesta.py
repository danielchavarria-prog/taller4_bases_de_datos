import requests
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:1000099027Dch@cluster0.mowkhwp.mongodb.net/?appName=Cluster0")
db = client["taller4_db"]
collection = db["raw_data"]

collection.drop()

BASE_URL = "https://thesimpsonsapi.com/api/characters"
characters = []
page = 1

print("Descargando personajes de The Simpsons API...")

while page <= 6:
    response = requests.get(BASE_URL, params={"page": page})
    
    if response.status_code != 200:
        print(f"Error en página {page}: {response.status_code}")
        break
    
    data = response.json()
    batch = data.get("results", [])
    
    if not batch:
        print(f"Página {page} vacía, deteniendo.")
        break
    
    characters.extend(batch)
    print(f"  Página {page}: {len(batch)} personajes descargados")
    page += 1

print(f"\nTotal descargado: {len(characters)} personajes")

if characters:
    result = collection.insert_many(characters)
    print(f"Insertados en MongoDB: {len(result.inserted_ids)} documentos")
    print(f"Base de datos: taller4_db | Colección: raw_data")
else:
    print("No se obtuvieron datos.")

client.close()