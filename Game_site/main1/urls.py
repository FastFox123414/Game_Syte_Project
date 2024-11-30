
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.About ),
    path('News/', views.News ),
    path('News_Game/', views.News_Game ),
    path('Reviews/', views.Reviews ),
    path('Ratings/', views.Ratings ),
]
