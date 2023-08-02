from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import TaskForm


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #commit=False
            #task = form.task
            #task.save()
            return redirect('home')
        else:
            error = 'Форма неверная'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'todo/create.html', context)


def home_view(request):
    tasks = Task.objects.order_by('id')
    user = request.user
    print(user, user)
    context = {
        'tasks' : tasks,
        'user' : user,
   }
    return render(request, 'todo/base.html', context)

def delete_task_view(request, task_id):
    task = get_object_or_404(Task, pk = task_id)
    print('Task_for_delete: ', task)
    task.delete()
    return redirect('home')
