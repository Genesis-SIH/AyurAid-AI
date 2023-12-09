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
# from django.db import models

# from db_connection import db

# class Data(models.Model):

#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     published = models.BooleanField(default=False)

#     class Meta:
#         managed = False
#         db_table = 'data'
#         collection = db['data']

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
       

