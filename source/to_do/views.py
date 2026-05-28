from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404

from to_do.models import Task


# Create your views here.
def main_page(request):
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'main_page.html', context)

def add_task(request):
    if request.method == 'GET':
        return render(request, 'add_task.html')
    elif request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        date = request.POST['date']

        Task.objects.create(
            title=title,
            description=description,
            status=status,
            date=date,
        )
        return HttpResponseRedirect('/')
    return None

def task(request, *args, pk, **kwargs):
    tasks = get_object_or_404(Task, pk=pk)
    context = {'task': tasks}
    return render(request, 'task.html', context)

