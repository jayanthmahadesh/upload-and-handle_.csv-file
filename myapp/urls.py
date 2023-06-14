from django.contrib import admin
from django.urls import path
from myapp import views
from .views import custom
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('custom/',custom.as_view(),name='custom'),
]
