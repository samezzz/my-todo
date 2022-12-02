from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_todo/<int:pk>', views.update_todo, name='update-todo'),
    path('update_todo/<int:pk>', views.delete_todo, name='delete-todo'),
    path('edit_todo/<int:pk>', views.edit_todo, name='edit-todo'),
]
