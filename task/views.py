from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm
from .models import Task


@login_required
def index(request):
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    q = request.GET.get('q')
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    if q:
        tasks = tasks.filter(title__icontains=q)
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(user_id=user_id, title=title, deadline=datetime.now().date())
    context = {
        'object_list': tasks
    }
    return render(request, 'task/index.html', context)


@login_required
def edit(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('.')
    context = {
        'form': form,
        'obj': task,
    }
    return render(request, 'task/edit.html', context)


@login_required
def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task:index')
    context = {
        'obj': task
    }
    return render(request, 'task/delete.html', context)

