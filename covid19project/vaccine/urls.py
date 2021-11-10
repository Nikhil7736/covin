from django.urls import path
from . import views

app_name = 'vaccine'

urlpatterns = [
    path('', views.home, name='home'),
]
