from django.contrib import admin
from user import models
# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.Department)
admin.site.register(models.Customer)
admin.site.register(models.Campuses)
admin.site.register(models.ClassList)