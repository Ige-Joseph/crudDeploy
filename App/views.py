from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Display list of tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# Create a new task
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(Title=title, decription=description)
        return redirect('task_list')
    return render(request, 'task_form.html')

# Update an existing task
def task_update(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        tasks.Title = request.POST.get('title')
        tasks.decription  = request.POST.get('description')
        tasks.completed = 'completed' in request.POST
        tasks.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'tasks': tasks})

# Delete a task
def task_delete(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        tasks.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'tasks': tasks})
