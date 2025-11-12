from django.urls import path
from .views import signupfunc, loginfunc,logoutfunc,listfunc,detailfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('list/',listfunc, name='list'),
    path('detail/<int:pk>',detailfunc, name='detail')
]
