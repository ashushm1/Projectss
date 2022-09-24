from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
#from django.views.decorators.csrf import csrf_protect
# Create your views here.

class FolderViewSet(ViewSet):
    def list(self,request):
        queryset = Folder.objects.all()
        serializer = FolderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request ,pk):
        try:
            folder = Folder.objects.get(pk=pk)
        except folder.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        Serializer = FolderSerializer(folder)
        return Response(Serializer.data)
    
    def delete(self,request, pk):
        try:
            folder=Folder.objects.get(pk=pk)
        except folder.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        folder.delete()
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self,request, pk):
        try:
            folder = Folder.objects.get(pk=pk)
        except folder.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    

class DocumentViewSet(ViewSet):
    def get(self,request):
        queryset = Document.objects.all()
        serializer = DocumentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk):
        try:
            document = Document.objects.get(pk=pk)
        except document.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        Serializer = DocumentSerializer(document)
        return Response(Serializer.data)
    
    def delete(self,request, pk):
        try:
            document=Document.objects.get(pk=pk)
        except document.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        document.delete()
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self,request,pk):
        try:
            document = Document.objects.get(pk=pk)
        except document.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    

class FileViewSet(ViewSet):
    def get(self,request):
        queryset = File.objects.all()
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk):
        try:
            file=File.objects.get(pk=pk)
        except file.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        Serializer = FileSerializer(file)
        return Response(Serializer.data)
    
    def delete(self, request, pk):
        try:
            file=File.objects.get(pk=pk)
        except file.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        file.delete()
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self,request,pk):
        try:
            file = File.objects.get(pk=pk)
        except file.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = FileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors)