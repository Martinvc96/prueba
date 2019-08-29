#prueba conexion MongoDB

import dns
from pymongo import MongoClient
from firebase import firebase
import pyrebase

#client = MongoClient("mongodb+srv://admin:admin@maincluster-rzyyj.mongodb.net/test?retryWrites=true&w=majority")

#db = client.get_database('hacht_DB')

#prueba = db.prueba

#count = prueba.count_documents({})

#print("Cantidad de registros: ",count)

#print("Registros encontrados:", list(prueba.find()))



#firebase = firebase.FirebaseApplication('https://inventario-ab622.firebaseio.com', None)

#result = firebase.get('/Users', None)

#print(result)


config = {
    "apiKey": "AIzaSyCfRRjL3jvA8pY0jJ_SdSwwW9SV2zsZFlg",
    "authDomain": "inventario-ab622.firebaseapp.com",
    "databaseURL": "https://inventario-ab622.firebaseio.com",
    "projectId": "inventario-ab622",
    "storageBucket": "inventario-ab622.appspot.com",
    "messagingSenderId": "933969484304",
    "appId": "1:933969484304:web:8e79e29e2b246ce9"
  }

    # initialize app with config
firebase = pyrebase.initialize_app(config)


db = firebase.database()

users = db.child("Users").get().each()
#print(users)


#data = {"email": "Mortimer@algo.com", "password": "yolo", "userName":"Mortimer 'Morty' Smith"}
#db.child("Users").push(data)

info = []
for user in users:
    info.append(user.val())
print(info)





