from django.urls import path
from .views import contact,index,about,bookDetails,new_book
urlpatterns = [
    path('',index,name='home'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('book_details/<int:book_id>/',bookDetails,name='book_details'),
    path('new_book/',new_book,name="new_book")
]