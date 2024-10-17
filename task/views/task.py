from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task.models import Task
from task.forms import TaskForm


class TaskListView(PermissionRequiredMixin, ListView):
    model = Task
    template_name = '01_task/task_list.html'
    permission_required = 'task.view_task'


class TaskAddView(PermissionRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = '01_task/task_add.html'
    success_url = reverse_lazy('home')
    permission_required = 'task.view_task'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            tasks=Task.objects.all()[:5]
        )


class TaskAttView(PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = '01_task/task_att.html'
    success_url = reverse_lazy('home')
    permission_required = 'task.view_task'


class TaskDelView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = '01_task/task_del.html'
    success_url = reverse_lazy('home')
    permission_required = 'task.view_task'

    def form_valid(self, form):
        self.object.register_task.all().delete()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)
