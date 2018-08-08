from django.contrib import admin
from .models import User, ConfirmString


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sex', 'c_time']
    list_filter = ['name', 'email', 'sex']
    search_fields = ['name', 'email', 'sex']


admin.site.register(User, UserAdmin)
admin.site.register(ConfirmString)
