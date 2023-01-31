from django.db import models
from fileapp.models import File
class Files(File.Model):
    # title= models.CharField(max_length=300)
    # description= models.CharField(max_length=300, unique=True, blank=True)

    # def __str__(self):
    #     return '%s %s' % (self.title, self.description)

    def search(self,query):
        return File.objects.filter(title__icontains=query)

