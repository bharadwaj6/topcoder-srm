from django.urls import path

from oceans import views

urlpatterns = [
    path('upload', views.upload_file, name='index'),
    path('upload_file', views.upload, name='upload'),
    path('push_upload', views.push_upload, name='push_upload'),
]
