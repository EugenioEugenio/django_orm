from django.urls import path
from . import views

urlpatterns = [
    # Маршрут по умолчанию для приложения todo
    path('', views.index, name='index'),
]

