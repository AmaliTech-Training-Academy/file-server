from django.contrib import admin
from authentication.models import CustomUser
from fileapp.models import File

class AuthAdmin(admin.ModelAdmin):
#     list_display = ('email')
    pass

admin.site.register(CustomUser,File, AuthAdmin)
