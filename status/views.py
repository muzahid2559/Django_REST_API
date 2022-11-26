from status.models import Status # Model
from .serializers import StatusSerializer # serializer based on status model


# building features
from rest_framework import generics, parsers


# Create your views here.

# status/ -> List, Create => GET, POST
class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


# status/<id> Details, Delete, Update => GET, DELETE, PUT/PATCH
class StatusDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    parser_classes = [parsers.FormParser, parsers.MultiPartParser]