# Implement Routings Here
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import new_task
from todolist.views import show_todolist_ajax


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('todolist', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', new_task, name='new_task'),
    path('json/',show_todolist_ajax, name='show_todolist_ajax'),
]