from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView
from user.models import User
from task.models import Task, Register

class HomeView(TemplateView):
    template_name = '01_task/home.html'
    #permission_required = 'task.view_task'
    
    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            users=User.objects.all(),
            tasks=Task.objects.all(),
            registers=Register.objects.all(),
            
        )
