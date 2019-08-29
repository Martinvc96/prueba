#prueba conexion MongoDB

import dns
#from pymongo import MongoClient
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
    "apiKey": "AIzaSyArQxRet5XqKI6v8948A2ZnHZOZsu7vCNY",
    "authDomain": "hacht-7d98d.firebaseapp.com",
    "databaseURL": "https://hacht-7d98d.firebaseio.com",
    "projectId": "hacht-7d98d",
    "storageBucket": "",
    "messagingSenderId": "225406534324",
    "appId": "1:225406534324:web:f5317f74d07ced54"
  }

    # initialize app with config
firebase = pyrebase.initialize_app(config)


db = firebase.database()

users = db.child("Users").get().each()
#print(users)

    ##USERS
#data = {"email": "prueba4@algo.com",
#        "name": "nombre4",
#        "org":"org4",
#        "password": "pass4",
#        "role": "2",
#        "salt": "salt4"}

    ##PACIENTE_A
#data = {"id_user": "user_id1",
#        "identificador": "nombre1",
#        "sexo":"m",
#        "edad": "20"}


    ##PACIENTE_D
#data = {"id_user": "user_id1",
#        "nombre": "nombre1",
#        "ced":"1",
#        "sexo": "f",
#        "edad": "20",
#        "res": "lugar1"}


    ##SESION
#data = {"id_paciente": "id1",
#        "fecha": "nombre4",
#        "obs":"org4",
#        "est": "pass4"}


    ##MUESTRA
#data = {"id_sesion": "id1",
#        "url_img": "url",
#        "pred":"org4",
#        "accuracy": "pass4",
#        "obs": "2",
#        "is_true": "salt4",
#        "consent": "algo1"}

#db.child("Muestra").push(data)

info = []
for user in users:
    info.append(user.val())
print(info)





