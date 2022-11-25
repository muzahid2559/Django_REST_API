from django.urls import path
from status import views

app_name = 'status'

# status/ -> List, Create => GET, POST
# status/<id> Details, Delete, Update => GET, DELETE, PUT/PATCH

urlpatterns = [
    path('status/', views.StatusListCreateView.as_view()),
    path('status/<id>/', views.StatusDetailAPIView.as_view()),


]