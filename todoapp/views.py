from django.shortcuts import render,redirect,get_object_or_404
from .models import *



def index(request):
    task = Task.objects.filter(is_completed = False)
    completed_task = Task.objects.filter(is_completed = True)
    context = {
        'task':task,
        'completed_task':completed_task,
    }
    return render(request,'index.html',context)


def add_task(request):
    tasks = request.POST['task']
    Task.objects.create(task=tasks)
    return redirect('index')


def mark_as_done(request, pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('index')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('index')


def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('index')
    else:
        context = {
            'get_task':get_task,
        }
    
    return render(request, 'edit_task.html',context)

def delete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('index')