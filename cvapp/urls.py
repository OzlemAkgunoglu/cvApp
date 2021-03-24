from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    ]