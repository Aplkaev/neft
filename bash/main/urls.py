from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index),
    path('upload',  views.upload_file),
    path('log', views.log)
]
