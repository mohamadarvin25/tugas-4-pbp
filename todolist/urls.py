from django.urls import path
from todolist.views import *
# from todolist.views import show_todolist
# from todolist.views import register
# from todolist.views import login_user
# from todolist.views import logout_user
# from todolist.views import create_task


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('hapus_task/<int:task_id>', hapus_task, name='hapus_task'),
    path('update_task/<int:task_id>', update_task, name='update_task'),
]