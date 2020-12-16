# from .views import video - this give the admin the opportunity of uploading the videos maually in the admin panel
from django.urls import path
from . import views


urlpatterns = [
    # path('', video), - this is the path for the admin panel video uplod
    path('', views.video, name='videopress'),
]
