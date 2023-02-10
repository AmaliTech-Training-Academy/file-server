from django.contrib import admin
from authentication.models import CustomUser

class AuthAdmin(admin.ModelAdmin):
#     list_display = ('email')
    pass

admin.site.register(CustomUser, AuthAdmin)
