from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

def list_of_todo_items(request):
    item_list = {'list': Todo.objects.all()}

    return render(request, 'todoApp/todoApp.htm', item_list)


def insert_todo_item(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todoApp/list/')

def delete_item(request, item_id):
    delete_todo_item = Todo.objects.get(id=item_id)
    delete_todo_item.delete()
    return redirect('/todoApp/list/')

