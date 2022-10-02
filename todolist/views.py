import datetime
from django.shortcuts import render

# Registrasi
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Login
from django.contrib.auth import authenticate, login

# Logout
from django.contrib.auth import logout
# Create your views here.

# Login required
from django.contrib.auth.decorators import login_required

# Cookies
from django.http import HttpResponseRedirect
from django.urls import reverse

from todolist.models import ItemTodolist

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    task = ItemTodolist.objects.filter(user=user)
    context = {
        'nama': user.username,
        'tasks': task
    }
    return render(request, "todolist.html", context)

# Register
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))  # membuat response
            currentDate = datetime.date.today()
            response.set_cookie('last_login',
                                str(currentDate.strftime("%Y-%m-%d")))  # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


def create_task(request):
    if (request.method == "POST"):
        title = request.POST["title"]
        currentDate = datetime.date.today()
        date = currentDate.strftime("%Y-%m-%d")
        description = request.POST["description"]
        task = ItemTodolist(user=request.user, title=title,date=date, description=description)
        task.save()
        return redirect('todolist:show_todolist')
    
    return render(request, 'create_task.html')

def hapus_task(request, task_id):
    deleted_item = ItemTodolist.objects.get(pk=task_id)
    deleted_item.delete()
    return redirect('todolist:show_todolist')

def update_task(request, task_id):
    updated_task = ItemTodolist.objects.get(pk=task_id)
    if updated_task.is_finished:
        updated_task.is_finished = False
    else:
        updated_task.is_finished = True
    updated_task.save()
    return redirect('todolist:show_todolist')