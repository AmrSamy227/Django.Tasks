from django.urls import path
from .views import *

urlpatterns = [
    path('', alltrainees),
    path('traineeid/', gettraineeid),
    path('Insert/', inserttrainee),
    path('Update/<int:id>', updatetrainee, name='updatetrainee'),
    path('Delete/<int:id>', deletetrainee, name='deletetrainee'),
]
