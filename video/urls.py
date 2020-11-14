from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('video/list', video_list, name='list'),
    path('video/new', video_new, name='new'),
    path('video/<int:video_id>/', video_detail, name='video_detail'),
]