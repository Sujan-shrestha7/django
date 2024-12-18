from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.http import JsonResponse
from .forms import BookForm


def index(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
 
def bookDetails(request,book_id):
    books=Book.objects.get(id=book_id)
    context={'books':books}
    return render (request,'book_details.html',context) 

def new_book(request):
    if request.method == "POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= BookForm()
    context = {'form':form}
    return render(request,'new_book.html',context)
