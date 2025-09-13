from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_library, name='video_library'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
]
