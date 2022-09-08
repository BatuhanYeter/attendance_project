from django.contrib import admin
from . import models

@admin.register(models.Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "age", "tck", "photourl", "phonenumber", "address")

@admin.register(models.Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    
@admin.register(models.Deletedworkers)
class DeletedWorkersAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "phonenumber", "tck",  "deletedate")
    
@admin.register(models.Entrances)
class EntrancesAdmin(admin.ModelAdmin):
    list_display = ("worker_id", "createddate")