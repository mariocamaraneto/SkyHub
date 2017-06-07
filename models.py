from db import db

class Photo(db.Document):
    url = db.StringField()
    path_large = db.StringField()
    path_medium = db.StringField()
    path_small = db.StringField()