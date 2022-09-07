from django.shortcuts import render
import serializers
from . import models
from rest_framework import status
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
 
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

import json

from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework.filterset import FilterSet

class WorkerFilter(FilterSet):
    class Meta(object):
        models = models.Workers
        fields = (
            'firstname', 'lastname', 'age', 'phone')

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticated],
)

class WorkersListView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin
):
    serializer_class = serializers.WorkerSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_class = WorkerFilter
    # permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id=None):
        if id:
            try:
                queryset = models.Workers.objects.get(id=id)
            except models.Workers.DoesNotExist:
                return Response({'errors': 'This worker does not exist.'}, status=400)
            read_serializer = serializers.WorkerSerializer(queryset)
        else:
            queryset = models.Workers.objects.all()
            read_serializer = serializers.WorkerSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = serializers.WorkerSerializer(data=request.data)
        
        if create_serializer.is_valid():
            worker_object = create_serializer.save()
            read_serializer = serializers.WorkerSerializer(worker_object)
            return Response(read_serializer.data, status=201)
        return Response(create_serializer.errors, status=400)

    def put(self, request, id=None):
        """
        Your docs
        ---
        # YAML (must be separated by `---`)
        serializer: WorkerSerializer

        parameters:
        - name: some_param
        description: Foobar long description goes here
        required: true
        type: integer
        paramType: form
        - name: other_foo
        paramType: query
        - name: avatar
        type: file
        """
        ...
        
        
        try:
            worker = models.Workers.objects.get(id=id)
        except models.Workers.DoesNotExist:
            return Response({'errors': 'This worker does not exist.'}, status=400)
        
        update_serializer = serializers.WorkerSerializer(worker, data=request.data)
        
        if update_serializer.is_valid():
            worker_object = update_serializer.save()
            read_serializer = serializers.WorkerSerializer(worker_object)
            return Response(read_serializer.data, status=200)
        return Response(update_serializer.errors, status=400)
    
    def delete(self, request, id=None):
        try:
            worker = models.Workers.objects.get(id=id)
        except models.Workers.DoesNotExist:
            return Response({'errors': 'This worker does not exist.'}, status=400)
        
        worker.delete()
        
        return Response(status=204)
    
    
class EntranceListView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin
):
    serializer_class = serializers.EntranceSerializer
    permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = {
    #     'worker': ["in", "exact"], # note the 'in' field
    #     'ean': ["exact"]
    # }
    
    def get(self, request, id=None):
        if id:
            try:
                queryset = models.Entrances.objects.all()
                entrances = queryset.filter(worker = id)
                read_serializer = serializers.EntranceSerializer(entrances, many=True)
                # queryset = models.Entrances.objects.get(worker=id)
            except models.Entrances.DoesNotExist:
                return Response({'errors': 'This worker does not exist.'}, status=400)
        else:
            queryset = models.Entrances.objects.all()
            read_serializer = serializers.EntranceSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = serializers.EntranceSerializer(data=request.data)
        
        if create_serializer.is_valid():
            employer_object = create_serializer.save()
            read_serializer = serializers.EntranceSerializer(employer_object)
            return Response(read_serializer.data, status=201)
        return Response(create_serializer.errors, status=400)
    
    def delete(self, request, id=None):
        try:
            employer = models.Entrances.objects.get(id=id)
        except models.Entrances.DoesNotExist:
            return Response({'errors': 'This worker does not exist.'}, status=400)
        
        employer.delete()
        
        return Response(status=204)    
    
    
class AddressListView(
    APIView
):
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        queryset = models.Addresses.objects.all()
        read_serializer = serializers.AddressSerializer(queryset, many=True)

        return Response(read_serializer.data)
    
    
class DeletedWorkersListView(
    APIView
):
    serializer_class = serializers.DeletedWorkerSerializer
    def get(self, request):
        queryset = models.Deletedworkers.objects.all()
        read_serializer = serializers.DeletedWorkerSerializer(queryset, many=True)

        return Response(read_serializer.data)

def index(request):
    context = {}
    return render(request, "index.html", context=context)
