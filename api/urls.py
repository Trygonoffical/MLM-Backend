
from django.urls import path
from . import views
urlpatterns = [
    path('config/', views.test, name='config'),
    
]
