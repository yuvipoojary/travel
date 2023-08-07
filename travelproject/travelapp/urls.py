from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('maths/', views.maths, name='maths'),
    # path('contact/', views.contact, name='contact')
]