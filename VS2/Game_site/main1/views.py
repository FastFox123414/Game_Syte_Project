from django.shortcuts import render

def Login(request):  
    return render(request, 'main1/login.html')
def About(request):
    return render(request,"main1/about.html")
def News(request):  
    return render(request, 'main1/news.html')
def News_Game(request):  
    return render(request, 'main1/newgames.html')
def Reviews(request):  
    return render(request, 'main1/reviews.html')
def Ratings(request):  
    return render(request, 'main1/ratings.html')

