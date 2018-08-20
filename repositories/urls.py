from django.urls import path
from . import views

urlpatterns= [
	path('', views.Repo, name='Repo'),
]