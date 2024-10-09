from django.urls import path, re_path
from .views import Framework

urlpatterns = [

    re_path(r'^.*\.html', Framework.as_view(), name='framework'),
    path('', Framework.as_view(), name='framework_dashboard'),

]