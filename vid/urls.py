from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_display_video, name='upload_display_video'),
]
