from django.db import models

class File(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='')
    downloads = models.IntegerField(default=0)
    emails_sent = models.IntegerField(default=0)
