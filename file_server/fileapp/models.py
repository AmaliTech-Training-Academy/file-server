from django.db import models

class File(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')
    downloads = models.IntegerField(default=0)
    
