from django.urls import path
from . import views 

app_name = 'modelo1'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]