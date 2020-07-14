from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('stats/<str:pk>/', views.statsView, name='stats'),
    path('statsdata/<str:pk>/', views.statsData, name="statsdata"),

    path('save_data/', views.saveData, name='save_data'),
]

