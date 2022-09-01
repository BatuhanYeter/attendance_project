# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from django.db import models
import os, uuid
from django.utils import timezone


class Addresses(models.Model):
    name = models.CharField(db_column='Name', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.

    def __str__(self):          
        return self.name
     
    class Meta:
        managed = False
        db_table = 'Addresses'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Deletedworkers(models.Model):
    old_id = models.IntegerField(db_column='Old_id', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    tck = models.CharField(db_column='TCK', unique=True, max_length=11, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True, max_length=10, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    addressid = models.ForeignKey(Addresses, models.DO_NOTHING, db_column='AddressId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    deletedate = models.DateTimeField(db_column='deleteDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deletedworkers'
        verbose_name = 'Deleted Workers'
        verbose_name_plural = 'Deleted Workers'



class Entrances(models.Model):
    worker = models.ForeignKey('Workers', models.DO_NOTHING, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Entrances'
        verbose_name = 'Entrance'
        verbose_name_plural = 'Entrances'

def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}.{}'.format(instance.pk, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid.uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)
        return wrapper

class Workers(models.Model):
    lastname = models.CharField(db_column='LastName', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    tck = models.CharField(db_column='TCK', unique=True, max_length=11, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    photourl = models.ImageField(db_column='PhotoUrl', upload_to=path_and_rename('images'))  # Field name made lowercase.
    # photo = models.FileField(upload_to=path_and_rename('images'))
    email = models.CharField(db_column='Email', max_length=255, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True, max_length=10, db_collation='Turkish_CI_AS')  # Field name made lowercase.
    address = models.ForeignKey(Addresses, models.DO_NOTHING, related_name="address", db_column='AddressId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate', default=datetime.now, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
    deletedate = models.DateTimeField(db_column='deleteDate', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):          
        return f'{self.firstname} {self.lastname}'
    class Meta:
        managed = False
        db_table = 'Workers'
        verbose_name = 'Workers'
        verbose_name_plural = 'Workers'
