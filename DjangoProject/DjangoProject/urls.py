
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("taskApp.urls")),
    path("signup/add/",include("taskApp.urls")),
    path("signup/",include("taskApp.urls")),
    path("forgot/",include("taskApp.urls")),
    path("forgot/search/<str:user>/<str:email>",include("taskApp.urls")),
    path("forgot/update/<str:user>/",include("taskApp.urls")),

]
