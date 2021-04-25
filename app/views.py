from django.views import generic
from django.shortcuts import render
from .models import Task


class TaskListView(generic.ListView):
    model = Task


def add_task(request):

    context = {
    }
    return render(request, 'app/add_task.html', context=context)
