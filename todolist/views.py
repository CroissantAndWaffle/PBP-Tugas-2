from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user.id)
    try:
        context = {
            'list_task': data_task,
            'name': 'Rafa Maritza',
            'studentid': '2106651944',
            'last_login': request.COOKIES['last_login'],
            'user': request.COOKIES['username'],
        }
        return render(request, "todolist.html", context)
    except KeyError:
        return redirect("/todolist/login/")

# @login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    # data = Task.objects.filter(user=request.user.id)
    data = Task.objects.filter(user=request.user.id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# @login_required(login_url='/todolist/login/')
# def show_todolist_ajax(request):
#     data_task = Task.objects.filter(user=request.user.id)
#     context = {
#         'list_task': data_task,
#         'name': 'Rafa Maritza',
#         'studentid': '2106651944',
#         'last_login': request.COOKIES['last_login'],
#         'user': request.COOKIES['username'],
#     }
#     return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('user', user.id)
            response.set_cookie('username', username)
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def new_task(request):
    if request.method == 'POST':
        uid = request.COOKIES['user']
        date = datetime.datetime.now()
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(user = User.objects.get(pk = uid), date=date, title=title, description=description)
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        return response
    context = {}
    return render(request, 'new_task.html', context)
