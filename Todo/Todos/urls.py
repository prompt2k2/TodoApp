from Todos.models import Tasks
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', views.index, name='todos-home'),
]
