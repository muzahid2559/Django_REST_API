from django.urls import path
from status import views

app_name = 'status'

urlpatterns = [
    path('api/', views.StatusAPIView.as_view(), name='api'),

]