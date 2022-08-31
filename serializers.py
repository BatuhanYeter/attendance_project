from dataclasses import fields
from rest_framework import serializers

from attendance import models

class AddressSerializer(serializers.ModelSerializer):     
    class Meta:
        model = models.Addresses
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        fields = ['id', 'name']
    

class WorkerSerializer(serializers.ModelSerializer):
    lastname = serializers.CharField(max_length=255) 
    firstname = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    tck = serializers.CharField(max_length = 11)
    photourl = serializers.ImageField()
    email = serializers.CharField(required=False)
    phonenumber = serializers.CharField(max_length = 10)
    # address = AddressSerializer()
    address = serializers.PrimaryKeyRelatedField(
        queryset=models.Addresses.objects.all())
    # createddate = serializers.DateTimeField(required=False)
    # updatedate = serializers.DateTimeField(required=False)
    # deletedate = serializers.DateTimeField(required=False)  
    
    class Meta:
        model = models.Workers
        fields = [
            'id',
            'lastname',
            'firstname',
            'age',
            'tck',
            'photourl',
            'email',
            'phonenumber',
            'address'
        ]
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
        
    def create(self, validated_data):
        return models.Workers.objects.create(
            lastname = validated_data.get("lastname"),
            firstname = validated_data.get("firstname"),
            age = validated_data.get("age"),
            tck = validated_data.get("tck"),
            photourl = validated_data.get("photourl"),
            email = validated_data.get("email"),
            phonenumber = validated_data.get("phonenumber"),
            address = validated_data.get("address"),
        )
    
    def update(self, instance, validated_data):
        models.Workers.objects.update(instance, validated_data)
        instance.save()
        return instance
    
    
        


class EntranceSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer(required=False)
    createddate = serializers.DateTimeField(required=False)  
    
    def create(self, validated_data):
        return models.Entrances.objects.create(
            worker = validated_data.get("worker"),
        )
    
    class Meta:
        model = models.Entrances
        fields = (
            'id',
            'worker',
            'createddate',
        )
        verbose_name = 'Entrance'
        verbose_name_plural = 'Entrances'