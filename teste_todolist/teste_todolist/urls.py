"""
URL configuration for teste_todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index, TodoList_View, Categoria_View, tarefa_add, categoria_add, tarefa_edit, categoria_edit, status_change, tarefa_remove, categoria_remove
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('tarefa_list', TodoList_View),
    path('categoria', Categoria_View),
    path('tarefa/add', tarefa_add, name='tarefa_add'),
    path('categoria/add', categoria_add, name='categoria_add'),

    path('/<int:id>/remove', tarefa_remove, name='tarefa_remove'),
    path('/<int:id>/remove_cat', categoria_remove, name='categoria_remove'),

    path('/<int:id_tarefa>/<int:id_status>/status',
         status_change, name='status_change'),
    path('tarefa/<int:id>/edit', tarefa_edit, name='tarefa_edit'),
    path('categoria/<int:id>/edit', categoria_edit, name='categoria_edit'),
]
