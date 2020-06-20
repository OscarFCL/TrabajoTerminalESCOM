from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from inscripcionTesis.views import *

urlpatterns = [
    path('vizualizarTesis', views.vertesis, name='vertesis'),
    path('inscripcionTesis', views.inscripcionTesisInicio, name='inscripcionTesisInicio'),
    path('tesisSimilares', views.tesisSimilares, name='tesisSimilares'),
    path('seleccionarProfesor', views.seleccionarProfesor, name='seleccionarProfesor'),
]