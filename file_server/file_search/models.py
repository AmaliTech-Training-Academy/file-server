from django.db import models
from fileapp.models import File
# Create your models here.
class File(File.Model):
    #name = models.CharField(max_length=100)

    def search(self, query):
        return File.objects.filter(title_icontains=query)
