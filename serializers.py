from dataclasses import fields
from rest_framework import serializers

from attendance import models

class AddressSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    
    class Meta:
        model = models.Addresses
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        fields = (
            'id',
            'name'
        )


class EmployerSerializer(serializers.ModelSerializer):
    lastname = serializers.CharField(max_length=255) 
    firstname = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    tck = serializers.CharField()
    photoid = serializers.CharField()
    email = serializers.CharField()
    phonenumber = serializers.CharField(max_length = 10)
    addressid = AddressSerializer(required=False)
    createddate = serializers.DateTimeField()
    updatedate = serializers.DateTimeField()
    deletedate = serializers.DateTimeField()  
    
    
    def create(self, validated_data):
        return models.Employers.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        models.Employers.objects.update(instance, validated_data)
        instance.save()
        return instance
    
    class Meta:
        model = models.Employers
        fields = (
            'id',
            'lastname',
            'firstname',
            'age',
            'tck',
            'photoid',
            'email',
            'phonenumber',
            'addressid',
            'createddate',
            'updatedate',
            'deletedate'
        )
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'
        
