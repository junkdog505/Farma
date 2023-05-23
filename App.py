import pyrebase
from firebase_admin import credentials

cred = credentials.Certificate("api/key.json")
firebase = pyrebase.initialize_app(cred)

db = firebase.database()

db.child(("names").push({"name": "Cristian"}))