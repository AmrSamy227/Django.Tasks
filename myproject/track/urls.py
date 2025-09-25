from django.urls import path
from .views import *
urlpatterns = [
    path('',alltracks,name='alltracks'),
    path('trackid/',gettrackid),
    path('Insert/',inserttrack),
    path('Update/<int:id>',updatetrack,name='updatetrack'),
    path('Dalete/<int:id>',deletetrack,name='deletetrack'),
]