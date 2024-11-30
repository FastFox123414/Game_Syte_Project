
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.about ),
    path('news', views.news ),
    path('newgames', views.newgames ),
    path('reviews', views.reviews ),
    path('ratings', views.ratings ),
    path('login',views.login)
]
