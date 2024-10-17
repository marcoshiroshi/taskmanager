from django.urls import path, include
from task.views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('task/add/', TaskAddView.as_view(), name="task_add"),
    path('task/<int:pk>/att/', TaskAttView.as_view(), name="task_att"),
    path('task/<int:pk>/del/', TaskDelView.as_view(), name="task_del"),
    path('task/list/', TaskListView.as_view(), name="task_list"),

    path('register/<int:pk>/add/', RegisterAddView.as_view(), name="register_add"),
    path('register/<int:pk>/att/', RegisterAttView.as_view(), name="register_att"),
    path('register/<int:pk>/del/', RegisterDelView.as_view(), name="register_del"),
    path('register/list/', RegisterListView.as_view(), name="register_list"),

]