from django.shortcuts import render
from django.http import HttpResponse

import dns
from pymongo import MongoClient

from firebase import firebase

import pyrebase



def helloFirebase(request):
    
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

    info = []
    for user in users:
        info.append(user.val())


    

    return HttpResponse(info)


def helloMongo(request):
    client = MongoClient("mongodb+srv://admin:admin@maincluster-rzyyj.mongodb.net/test?retryWrites=true&w=majority")

    db = client.get_database('hacht_DB')

    prueba = db.prueba

    #count = prueba.count_documents({})
    #print("Cantidad de registros: ",count)

    #print("Registros encontrados:", list(prueba.find()))

    return HttpResponse(list(prueba.find()))

def index(request):
  return render(
        request,
        'index.html',
        context={},
    )