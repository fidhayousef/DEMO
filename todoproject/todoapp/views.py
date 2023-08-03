from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskListView(ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "task1"
class TaskDetailView(DetailView):
    model = Task
    template_name = "detail.html"
    context_object_name = "task"
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "edit.html"
    context_object_name = "task"
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id })
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request,"home.html",{'task': task1})


def delete(request, taskid):
    if request.method == 'POST':
        task=Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request,id):
    task_update = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task_update)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update.html", {'form': form, 'task_update': task_update})
