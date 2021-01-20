from django.urls import path
from . import views

app_name ='encuestas'

urlpatterns=[
    path('', views.indice),
    path('/new', views.nuevo)
]