from pymongo import MongoClient
import random

MONGO_URI = "mongodb://mongo-bayeta:27017/"
DB_NAME = "bayeta"
COLLECTION_NAME = "frases"


def get_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]


def inicializar_frases():
    col = get_collection()

    if col.count_documents({}) == 0:
        with open("frases.txt", "r", encoding="utf-8") as f:
            frases = [{"texto": line.strip()} for line in f if line.strip()]

        if frases:
            col.insert_many(frases)


def obtener_frases(n=1):
    col = get_collection()
    documentos = list(col.find())

    if not documentos:
        return []

    return [random.choice(documentos)["texto"] for _ in range(n)]
