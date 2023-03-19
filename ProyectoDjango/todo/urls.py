from django.contrib import admin
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('agregar/', views.agregar,name='agregar'),
]
#urlpatterns = [
#    path('admin/',admin.site.urls),
#    path('',views.home,name='home'),
#    path('agregar/',views.agregar,name='agregar'),
#]


#from django.contrib import admin
#from django.urls import path, include
#from todo import views

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include("todo.urls")),
#    path('', views.home,name="home"),
#    path("eliminar/<int:tarea_id>/", views.eliminar, name = 'eliminar'),
#    path("editar/<int:tarea_id>/", views.editar, name = 'editar'),
#]
