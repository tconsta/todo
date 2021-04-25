from django.views import generic

from .models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreate(generic.CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'app/task_create.html'
    success_url = '/'
