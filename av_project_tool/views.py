from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task # Ensure Task is imported
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def project_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = TaskForm()
        
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects, 'form': form})

# ADD THIS FUNCTION BELOW YOUR project_list FUNCTION:
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('project_list')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_list')
        else:
            form = TaskForm(instance=task)
        return render(request, 'edit_task.html', {'form': form, 'task': task})