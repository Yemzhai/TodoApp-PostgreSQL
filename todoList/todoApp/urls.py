from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.list_of_todo_items),
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item')
]
