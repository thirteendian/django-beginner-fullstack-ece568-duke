from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def djlogin(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':

        name = request.POST.get('name')
        password = request.POST.get('password')
        # 验证用户名和密码，验证通过的话，返回user对象
        user = auth.authenticate(username=name, password=password)
        if user:
            # 验证成功 登陆
            auth.login(request, user)
            return HttpResponseRedirect('home.html')
        else:
            return render(request, 'userRegister.html')
            