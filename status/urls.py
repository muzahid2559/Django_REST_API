from django.urls import path
from status import views

app_name = 'status'

urlpatterns = [
    path('status/', views.StatusAPIView.as_view(), name='api'),
    path('status/list/', views.StatusListAPIView.as_view(), name='list_api'),
    path('status/create/', views.StatusCreateAPIView.as_view()),

]