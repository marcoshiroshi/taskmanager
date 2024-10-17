from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task.models import Task, Register
from task.forms import RegisterForm


class RegisterListView(PermissionRequiredMixin, ListView):
    model = Register
    template_name = '01_task/register_list.html'
    permission_required = 'task.view_task'

    # def get_queryset(self):
    #     return Register.objects.filter(user=self.request.user)


class RegisterAddView(PermissionRequiredMixin, CreateView):
    model = Register
    form_class = RegisterForm
    template_name = '01_task/register_add.html'
    permission_required = 'task.view_task'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            task=Task.objects.get(id=self.kwargs.get('pk'))
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.task = Task.objects.get(id=self.kwargs.get('pk'))
        self.object.save()
        return HttpResponseRedirect(reverse('register_add', args=[self.object.task.id]))


class RegisterAttView(PermissionRequiredMixin, UpdateView):
    model = Register
    form_class = RegisterForm
    template_name = '01_task/register_att.html'
    permission_required = 'task.view_task'

    def get_success_url(self):
        return reverse('register_att', args=[self.object.id])


class RegisterDelView(PermissionRequiredMixin, DeleteView):
    model = Register
    template_name = '01_task/register_del.html'
    success_url = reverse_lazy('home')
    permission_required = 'task.view_task'

    def get_success_url(self):
        return reverse('register_add', args=[self.object.task.id])
