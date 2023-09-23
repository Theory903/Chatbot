from django.shortcuts import render
# Create your views here.
def home(request):
     return render(request,'bot.html')
def login(request):
     return render(request,'login.html')
def logout(request):
     return render(request,'logout.html')
def forg(request):
     return render(request,'forg.html')
def settings(request):
     return render(request,'settings.html')
def Activity(request):
     return render(request,'Activity.html')
