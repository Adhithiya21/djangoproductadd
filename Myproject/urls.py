"""
URL configuration for Myproject project.

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
from Myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.demo),
    # path('new',views.nfunc),
    # path('demo',views.demo1),
    # path('check',views.func),
    # path('fun',views.fun1),
    # path('hit',views.fun2),
    # path('readd',views.reads,name='read'),
    # path('create',views.create,name='create'),
    # path('delete/<int:id>',views.delete,name='delete'),
    # path('update/<int:id>',views.update,name='update'),
    # path('emreadd',views.search_and_read,name='reads'),
    # path('emcreate',views.emcreate,name='create'),
    # path('emdelete/<int:id>',views.emdelete,name='emdelete'),
    # path('emupdate/<int:id>',views.emupdate,name='emupdate'),
    path('prreadd',views.search_and_read,name='reads'),
    path('prcreate',views.prcreate,name='create'),
    path('prdelete/<int:id>',views.prdelete,name='prdelete'),
    path('prupdate/<int:id>',views.prupdate,name='prupdate'),
]


