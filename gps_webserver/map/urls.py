from django.urls import path, include

from . import views

#tells the program where to go when it receives a url from mysite
urlpatterns = [
    path("", views.main_screen, name="main-screen"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("main-screen", views.main_screen, name="main-screen"),
    path("positions", views.positions, name="positions"),
]
