from multiprocessing import context
from django.shortcuts import render
from rest_framework import viewsets
from api.models import client,project,user
from api.serializers import ClientSerializers,projectSerializer,UserSerializers
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
  queryset=user.objects.all()
  serializer_class=UserSerializers
  
# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
  queryset=client.objects.all()
  serializer_class=ClientSerializers 
  
#clients/id/projects
  @action(detail=True,methods=['get'] )
  def projects(self,request,pk=None):
     try:
        client=client.objects.get(pk=pk)
        prjs=project.objects.filter(client=client)
        prjs_serializers=projectSerializer(prjs,many=True,context={'request':request})
        return Response(prjs_serializers.data)
     except  Exception as e :
      print(e)
      return Response({
        'message':'client might not exists !! error'
      }) 

class projectViewSet(viewsets.ModelViewSet):
    queryset=project.objects.all()
    serializer_class=projectSerializer