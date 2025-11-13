from django.urls import path
from .views import signupfunc, loginfunc,logoutfunc,listfunc,detailfunc,goodfunc,subscribefunc,SNSCreate

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('list/',listfunc, name='list'),
    path('detail/<int:pk>',detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name="good"),
    path('subscribe/<int:pk>', subscribefunc, name='subscribe'),
    path('create/', SNSCreate.as_view(), name='create'),
]
