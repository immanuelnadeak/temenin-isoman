from collections import namedtuple
from django.urls import path

from emergency_contact.views import *

urlpatterns = [
    path('', index, name='emergency-contact'),
    path('add-daerah', add_daerah),
    path('add-rs', add_rs),
    path('daerah_json',  daerah_json),
    path('rs_json',  rs_json),
    path('update_rs/<str:pk>/',  update_rs),
    path('hapus_rs/<str:pk>/',  hapus_rs),
    path('update_daerah/<str:pk>/',  update_daerah),
    path('hapus_daerah/<str:pk>/',  hapus_daerah)
]