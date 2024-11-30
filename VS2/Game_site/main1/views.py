from django.shortcuts import render

def login(request):  
    return render(request, 'main1/login.html')
def about(request):
    return render(request,"main1/about.html")
def news(request):  
    return render(request, 'main1/news.html')
def newgames(request):  
    return render(request, 'main1/newgames.html')
def reviews(request):  
    return render(request, 'main1/reviews.html')
def ratings(request):  
    return render(request, 'main1/ratings.html')

