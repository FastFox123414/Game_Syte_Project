from django.shortcuts import render

def About(request):
    return render(request,"main1/About.html")
def News(request):  
    return render(request, 'main1/News.html')
def News_Game(request):  
    return render(request, 'main1/News_Game.html')
def Reviews(request):  
    return render(request, 'main1/reviews.html')
def Ratings(request):  
    return render(request, 'main1/ratings.html')