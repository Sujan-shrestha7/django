from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def index(request):
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("<h1> this is contact route </h1>")  

def about(request):
    return HttpResponse("this is about route")     

