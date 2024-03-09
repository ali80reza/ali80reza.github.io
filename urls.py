from django.urls import path
from .views import about,whatsapp,instagram

app_name = 'core'

urlpatterns = [
    path('about/' , about , name='about'),
    path('whatsapp/' , whatsapp , name='whatsapp'),
    path('instagram/' , instagram , name='instagram'),
]