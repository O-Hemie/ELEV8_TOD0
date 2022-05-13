# urls files for todoapp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('log', views.log, name='log'),
    path('profile', views.profile, name='profile'),
    path('sign', views.sign, name='sign'),
    path('edit', views.edit, name='edit'),
    path('add_task', views.add_task, name= 'add_task'),
    path('delete', views.delete, name='delete'),
    path('edittask', views.edittask, name='edittask')
]

