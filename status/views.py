from status.models import Status # Model
from .serializers import StatusSerializer # serializer based on status model


# building features
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, mixins


# Create your views here.

# status/ -> List, Create => GET, POST
class StatusListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# status/<id> Details, Delete, Update => GET, DELETE, PUT/PATCH
class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

