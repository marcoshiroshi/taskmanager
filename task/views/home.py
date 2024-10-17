from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, TemplateView
from user.models import User
from task.models import Task, Register


class HomeView(PermissionRequiredMixin, TemplateView):
    template_name = '01_task/home.html'
    permission_required = 'task.view_task'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.all()
        return dict(
            super().get_context_data(**kwargs),
            # exemplos de querysets
            common_tasks=tasks.exclude(user=self.request.user)[:5],
            user_tasks=tasks.filter(user=self.request.user)[:5],
            tasks=tasks,
            users=User.objects.all(),
            registers=Register.objects.all(),
        )
