from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView


class HomeView(PermissionRequiredMixin, TemplateView):
    template_name = '01_task/home.html'
    permission_required = 'task.view_task'
