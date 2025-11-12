from django.shortcuts import render
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(request.POST)
        password = request.POST['password']
        user = User.objects.create_user(username,'',password)
        user.save()
        
    return render(request, 'signup.html')