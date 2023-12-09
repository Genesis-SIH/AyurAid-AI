from django.db import models

from db_connection import db
# Create your models here.



class Data:

    def __init__(self, title, description, published):
        self.title = title
        self.description = description
        self.published = published

    def save(self):
        db.data.insert_one({
            "title": self.title,
            "description": self.description,
            "published": self.published
        })
