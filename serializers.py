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


class WorkerSerializer(serializers.ModelSerializer):
    lastname = serializers.CharField(max_length=255) 
    firstname = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    tck = serializers.CharField(max_length = 11)
    photoid = serializers.CharField()
    email = serializers.CharField(required=False)
    phonenumber = serializers.CharField(max_length = 10)
    addressid = AddressSerializer(required=False)
    createddate = serializers.DateTimeField(required=False)
    updatedate = serializers.DateTimeField(required=False)
    deletedate = serializers.DateTimeField(required=False)  
    
    
    def create(self, validated_data):
        return models.Workers.objects.create(
            lastname = validated_data.get("lastname"),
            firstname = validated_data.get("firstname"),
            age = validated_data.get("age"),
            tck = validated_data.get("tck"),
            photoid = validated_data.get("photoid"),
            email = validated_data.get("email"),
            phonenumber = validated_data.get("phonenumber"),
            addressid = validated_data.get("addressid"),
        )
    
    def update(self, instance, validated_data):
        models.Workers.objects.update(instance, validated_data)
        instance.save()
        return instance
    
    class Meta:
        model = models.Workers
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
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
        
