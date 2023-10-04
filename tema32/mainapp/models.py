from django.db import models
from datetime import datetime

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Books"