from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404, redirect

from to_do.models import Task
from to_do.forms import TaskForm


def main_page(request):
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'task/main_page.html', context)



def add_task(request):
    form = TaskForm()

    if request.method == 'GET':
        return render(request, 'task/add_task.html', {'form': form})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')

        return render(request, 'task/add_task.html', {'form': form})
    return None

def update_task(request, pk, *args, **kwargs):

    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'task/update_task.html', {'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            
            return redirect('/')
        return render(request, 'task/update_task.html', {'form': form, 'task': task})




        # task.title = request.POST['title']
        # task.description = request.POST['description']
        # task.detail_description = request.POST['detail_description']
        # task.status = request.POST['status']
        # task.date = request.POST['date'] or None

        task.save()
    return HttpResponseRedirect('/')


def task(request, *args, pk, **kwargs)  :
    tasks = get_object_or_404(Task, pk=pk)
    context = {'task': tasks}
    return render(request, 'task/task.html', context)

def detail_task(request, *args, pk, **kwargs):
    tasks = get_object_or_404(Task, pk=pk)
    context = {'task': tasks}
    return render(request, 'task/detail_description.html', context)

def delete_task(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, "task/delete_task.html", {'task': task})
    elif request.method == "POST":
        task.delete()
    return HttpResponseRedirect('/')