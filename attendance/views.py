from django.shortcuts import render
import serializers
from . import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin


class EmployersListView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin
):
    def get(self, request, id=None):
        if id:
            try:
                queryset = models.Employers.objects.get(id=id)
                print(f'----------> {queryset}')
            except models.Employers.DoesNotExist:
                return Response({'errors': 'This employer does not exist.'}, status=400)
            read_serializer = serializers.EmployerSerializer(queryset)
        else:
            queryset = models.Employers.objects.all()
            read_serializer = serializers.EmployerSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = serializers.EmployerSerializer(data=request.data)
        
        if create_serializer.is_valid():
            employer_object = create_serializer.save()
            read_serializer = serializers.EmployerSerializer(employer_object)
            return Response(read_serializer.data, status=201)
        return Response(create_serializer.errors, status=400)

    def put(self, request, id=None):
        try:
            employer = models.Employers.objects.get(id=id)
        except models.Employers.DoesNotExist:
            return Response({'errors': 'This employer does not exist.'}, status=400)
        
        update_serializer = serializers.EmployerSerializer(employer, data=request.data)
        
        if update_serializer.is_valid():
            employer_object = update_serializer.save()
            read_serializer = serializers.EmployerSerializer(employer_object)
            return Response(read_serializer.data, status=200)
        return Response(update_serializer.errors, status=400)
    
    def delete(self, request, id=None):
        try:
            employer = models.Employers.objects.get(id=id)
        except models.Employers.DoesNotExist:
            return Response({'errors': 'This employer does not exist.'}, status=400)
        
        employer.delete()
        
        return Response(status=204)