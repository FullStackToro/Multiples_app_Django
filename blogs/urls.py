from django.urls import path
from . import views

app_name='blogs'

urlpatterns=[
    path('', views.indice, name='index'),
    path('/new', views.nuevo),
    path('/create', views.crear),
    path('/<int:my_val>', views.show),
    path('/<int:my_val>/editar', views.editar),
    path('/<int:my_val>/destruir', views.destruir)

]