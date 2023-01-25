from django.contrib import admin
from fileapp.models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'downloads','emails_sent')

admin.site.register(File, FileAdmin)

