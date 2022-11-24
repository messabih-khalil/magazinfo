from django.db import models
from base_classes import baseModels as base
# Create your models here.

class Audio(base.BaseModel):
    # image
    image = models.ImageField(upload_to='audio/images')
    # file
    file = models.FileField(upload_to='audio/files', blank=False)

