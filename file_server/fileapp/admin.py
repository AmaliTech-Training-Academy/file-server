from django.contrib import admin
from authentication.models import CustomUser
from fileapp.models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'downloads','emails_sent')

admin.site.register(CustomUser, File, FileAdmin)

 