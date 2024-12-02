
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home ),
    path('News/', views.News ),
    path('News_Game/', views.News_Game ),
    path('Reviews/', views.Reviews ),
    path('Ratings/', views.Ratings ),
    path('login/', views.Login ),
]
