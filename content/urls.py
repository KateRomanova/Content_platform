from django.urls import path
from content.apps import ContentConfig
from content.views import home

app_name = ContentConfig.name

urlpatterns = [
    path('', home, name='home')
]
