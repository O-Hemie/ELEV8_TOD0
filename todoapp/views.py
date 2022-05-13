from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
def home(request):
    '''Renders the home page when the user is logged in'''
    my_tasks = Task.objects.all()
    return render(request, 'users.html', {'my_tasks':my_tasks})

def index(request):
    '''Returns the index page'''
    return render(request, 'index.html')

def log(request):
    '''Returns the login page'''
    return render(request, 'log.html')

def profile(request):
    '''Returns the profile page'''
    return render(request, 'profile.html')

def sign(request):
    '''Returns the sign page'''
    return render(request, 'sign.html')

def edit(request):
    '''Returns the edit page'''
    return render(request, 'edit.html')

def add_task(request):
    '''Add a task to the database'''
    if request.method == 'POST':
        task_passed = request.POST.get('task')
        if task_passed != '': 
            new_task =Task()
            new_task.name = task_passed
            new_task.save()
    return redirect('home')

def delete(request):
    '''Delete a task from the database'''
    deleted_item  = request.GET.get('item_to_delete')
    del_item =Task.objects.get(id= deleted_item)
    del_item.delete()
    return redirect('home')

def edittask(request):
    '''Edit a task in the database'''
    if request.method == 'POST':
        edited_text = request.POST.get('edit_text')
        edited_id = request.POST.get('edit_id')
        task_to_edit = Task.objects.get(id= edited_id)
        task_to_edit.name = edited_text
        task_to_edit.save()
    return redirect ('home')