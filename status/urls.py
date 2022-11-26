from django.urls import path
from status import views
from rest_framework.routers import DefaultRouter


# status/ -> List, Create => GET, POST
# status/<id> Details, Delete, Update => GET, DELETE, PUT/PATCH

router = DefaultRouter()
router.register(r'status', views.StatusViewset, basename='status')


urlpatterns = [] + router.urls