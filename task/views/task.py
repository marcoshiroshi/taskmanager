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

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskAddView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = '01_task/task_add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            tasks=Task.objects.all()
        )

'''


class TaskAttView(PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = '01_task/task.html'
    success_url = reverse_lazy('task_meus_dados')
    permission_required = 'task.view_task'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        if self.object.._Task.filter(sede=True).exists():
                self.object..ck_Task = True
        else:
            self.object..ck_Task = False
        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"": self.request.user.task_inst_user})
        return kwargs


class TaskDelView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = '01_task/task_del.html'
    success_url = reverse_lazy('task_meus_dados')
    permission_required = 'task.view_task'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            form=TaskForm(self.request.POST or None, instance=self.get_object()),
        )

    def form_valid(self, form):
        if self.object.sede:
            self.object..ck_Task = False
            self.object..save()
        self.object.delete()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

'''
        