
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home ),
    path('News/', views.News ),
    path('News_Game/', views.News_Game ),
    path('Reviews/', views.Review ),
    path('Ratings/', views.Rating ),
    path('login/', views.Login ),
    path('registr/', views.Registr , name="registr" ),
    path('Password_Rec/', views.Password_Rec ),
    path('Private_account/', views.Private_account_view ,name="Private_account"),
    
]
