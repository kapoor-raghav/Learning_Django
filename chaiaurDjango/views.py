from django.http import HttpResponse
from  django.shortcuts import render

def home(request):
    ## return HttpResponse("hello, world. you are at chai aur Django Home page")
    return render(request,'website/index.html')

def about(request):
    ## return HttpResponse("hello, world. you are at chai aur Django about page")
    return render(request,'website/about.html')

def contact(request):
    ## return HttpResponse("hello, world. you are at chai aur Django contact page")
    return render(request,'website/contact.html')