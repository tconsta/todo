from django.views import generic

from .models import Task


class TaskListView(generic.ListView):
    model = Task
