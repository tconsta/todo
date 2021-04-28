from django.views import generic
from django.shortcuts import redirect
from .models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreate(generic.CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'app/task_create.html'
    success_url = '/'


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = '/'


class TaskUpdate(generic.UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = '/'


def done_undone(request, pk):
    task = Task.objects.get(pk=pk)
    if task.completed is True:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return redirect('/')
