
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("signup/add/",views.addUser,name='addUser'),
    path("signup/",views.signup,name='signup'),
    path("forgot/",views.forgot,name='forgot'),
    path("forgot/search/<str:user>/<str:email>",views.searchUser,name='search'),
    path("forgot/update/<str:user>/",views.updatePass,name='pass'),
]