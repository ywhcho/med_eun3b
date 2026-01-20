from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    path('', views.index, name='index'),
    path('by-ingredient/', views.by_ingredient, name='by_ingredient'),
    path('by-company/', views.by_company, name='by_company'),
    path('by-effect/', views.by_effect, name='by_effect'),
    path('<int:pk>/', views.detail, name='detail'),
]
