from status.models import Status # Model
from .serializers import StatusSerializer # serializer based on status model


# building features
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, mixins


# Create your views here.

# status/ -> List, Create => GET, POST
class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# status/<id> Details, Delete, Update => GET, DELETE, PUT/PATCH
class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'