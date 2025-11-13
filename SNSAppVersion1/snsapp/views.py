from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import SnsModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.create_user(username2, '', password2)
            return render(request, 'signup.html', {'success':'Complete Sign Up'})
        except:
            return render(request, 'signup.html', {'error':'username already exists'})
        
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
             return redirect('login')
        
    return render(request, 'login.html')

@login_required
def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def listfunc(request):
    sns_list = SnsModel.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'sns_list': sns_list})

@login_required
def detailfunc(request, pk):
    sns_item = SnsModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'sns_item': sns_item})

@login_required
def goodfunc(request, pk):
    sns_item = SnsModel.objects.get(pk=pk)
    sns_item.good += 1
    sns_item.save()
    return JsonResponse({'good': sns_item.good})

@login_required
def subscribefunc(request, pk):
    sns_item = SnsModel.objects.get(pk=pk)
    if(sns_item.subscribe==False):
        sns_item.subscribe =True
        sns_item.save()
    else:
        sns_item.subscribe =False
        sns_item.save()
    
    return JsonResponse({'subscribe': sns_item.subscribe})

class SNSCreate(CreateView):
    template_name = 'create.html'
    model = SnsModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')
