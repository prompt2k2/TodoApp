from Todos.models import Tasks
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', views.index, name='todos-home'),
    path('add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
]
