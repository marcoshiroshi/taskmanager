from django.urls import path, include
from task.views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('task_add/', TaskAddView.as_view(), name="task_add"),
    
]