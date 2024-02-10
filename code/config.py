import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def initFirestone():
    cred = credentials.Certificate('team6Key.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
