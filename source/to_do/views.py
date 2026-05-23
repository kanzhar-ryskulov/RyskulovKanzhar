from django.shortcuts import render

from to_do.models import Task


# Create your views here.
def main_page(request):
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'main_page.html', context)