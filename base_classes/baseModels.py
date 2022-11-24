from django.db import models

# Create your models here.

class BaseModel(models.Model):
    title = models.CharField(null=False , blank=False , max_length=255)
    description = models.TextField(null=True , blank=True)
    author = models.CharField(null = True , blank= True , max_length=255)
    created_at = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        abstract = True