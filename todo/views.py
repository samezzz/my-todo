from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method != "POST":
        form = TodoModelForm()
        todos = Todo.objects.all()
    else:
        finished = request.POST.get('is_finished', "Not Finished")
        if not finished:
            finished = "Finished"
        active = request.POST.get('active', "True")
        if not active:
            active = False
            
        form = TodoModelForm(request.POST)
        if form.is_valid():
            todos = Todo(
                title = request.POST['title'],
                is_finished = finished,
                due_date = request.POST['due_date'],
                due_time = request.POST['due_time'],
            )
            if todos.due_time and todos.due_date != "":
                todos.save()
            else:
                todos = Todo(
                    title = request.POST['title'],
                is_finished = finished,
                )
                todos.save()
            return redirect('index')
        todos.save()
        todos = Todo.objects.all()
    
    context = {
        'todos': todos,
        'form': form,
        
    }
    return render(request, 'todo/index.html', context)

def update_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST" or "None":
        if todo.is_finished == "Finished":
            todo.is_finished = "Not Finished"
        else:
            todo.is_finished = "Finished"
        if todo.active:
            todo.active = False
        else:
            todo.active = True
        todo.save()
        return redirect('index')
    
def delete_todo(request, pk=None):
    todo = Todo.objects.get(id=pk).delete()
    return redirect("index")

def edit_todo(request, pk=None):  
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        edited_todo = Todo(
            title = request.POST['title'],
        )
        todo.title = edited_todo.title
        todo.save()
        return redirect('index')
    
    context = {
        "todo": todo,
    }
    return render(request, 'todo/edit_todo.html', context)
        
        