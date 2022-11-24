from django.db import models
from base_classes import baseModels as base
# Create your models here.


class Book(base.BaseModel):
    # image
    image = models.ImageField(upload_to='books/images')
    # file
    file = models.FileField(upload_to='books/files', blank=False)