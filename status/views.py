from status.models import Status # Model
from .serializers import StatusSerializer # serializer based on status model


# building features
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class StatusAPIView(APIView):

    def get(self, request, format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)
        return Response(status_serializer.data)