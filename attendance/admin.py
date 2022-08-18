from django.contrib import admin
from . import models

@admin.register(models.Employers)
class EmployersAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "age", "tck", "photoid", "phonenumber", "addressid")

@admin.register(models.Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    
@admin.register(models.Deletedemployers)
class DeletedEmployersAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "phonenumber", "tck",  "deletedate")