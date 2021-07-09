from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('login', views.login,name="login"),
    path('escultura', views.escultura,name="escultura"),
    path('tejido', views.tejido,name="tejido"),
    path('orfebreria', views.orfebreria,name="orfebreria"),
    path('pintura', views.pintura,name="pintura"),
    path('contacto', views.contacto,name="contacto"),
    path('agregar', views.agregar,name="agregar"),
    path('registro', views.registro,name="registro"),
    path('admin', views.admin,name="admin"),
    path('tablacrud', views.tablacrud,name="tablacrud"),
    path('agregarcrud/', views.agregarcrud,name="agregarcrud"),
    path('registrof', views.registrof,name="registrof"),
]