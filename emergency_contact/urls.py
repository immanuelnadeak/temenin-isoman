from collections import namedtuple
from django.urls import path

from emergency_contact.views import daerah_json, index, add_daerah, add_rs

urlpatterns = [
    path('', index, name='emergency-contact'),
    path('add-daerah', add_daerah),
    path('add-rs', add_rs),
    path('daerah_json',  daerah_json)
]