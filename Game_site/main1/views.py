from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render , redirect
from .models import New
from .models import New_Game
from .models import Reviews
from .models import Ratings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views.generic import DetailView
def home(request):
    return render(request,"main1/home.html")
def News(request):  
    news = New.objects.order_by("-date")[:1]
    return render(request, 'main1/News.html',{"news":news})
def News_Game(request):
    new_game1 = New_Game.objects.order_by("-date")[:1]
    new_game2 = New_Game.objects.order_by("-date")[1:2]
    new_game3 = New_Game.objects.order_by("-date")[2:3]
    return render(request, 'main1/News_Game.html',{"new_game1":new_game1,"new_game2":new_game2,"new_game3":new_game3})
def Review(request):  
    Rev = Reviews.objects.order_by("-id")[:1]
    return render(request, 'main1/reviews.html',{"Rev":Rev})
def Rating(request):  
    Rating1 = Ratings.objects.order_by("-id")[:1]
    Rating2 = Ratings.objects.order_by("-id")[1:2]
    Rating3 = Ratings.objects.order_by("-id")[2:3]
    return render(request, 'main1/ratings.html',{"Rating1":Rating1,"Rating2":Rating2,"Rating3":Rating3})
def Login(request):  
    return render(request, 'main1/login.html')
def Registr(request):  
    return render(request, 'main1/registr.html')
def Password_Rec(request):  
    return render(request, 'main1/Password_Rec.html')
def Private_account(request):  
    return render(request, 'main1/private_account.html')

@login_required
def Private_account_view(request):
    return render(request, "main1/private_account.html")

class RegisterUser(DetailView ,CreateView):
    form_class = UserCreationForm
    template_name = "main1/registration/registr.html"
    success_url = reverse_lazy("login")
    
    def get_context_data(self, *, object_list=None , **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()) )
    
    