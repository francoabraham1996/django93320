from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('pinturas/', views.listado_de_pinturas)
]