from django.urls import path
from . import views

# Cuando el usuario ingrese a la url estara en inicio
urlpatterns = [
    path('', views.inicio, name='inicio'),
# Con esto accedemos vía url y mostraremos el hml de nosotros
    path('nosotros', views.nosotros, name='nosotros')
]