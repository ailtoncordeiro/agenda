from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('agenda/', views.list_eventos),
    path('agenda/evento/',views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/',views.delete_evento),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]
