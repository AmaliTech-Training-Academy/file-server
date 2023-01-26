from django.db import models
class Files(files.Model):
    title= models.CharField(max_length=300)
    description= models.CharField(max_length=300, unique=True, blank=True)
    def__str__(self,description):
        return self.description

    def__str__(self,title):
        return self.title
