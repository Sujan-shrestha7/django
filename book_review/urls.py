from django.urls import path
from .views import contact,index,about,bookDetails,new_book,delete_book,edit_book
urlpatterns = [
    path('',index,name='home'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('book_details/<int:book_id>/',bookDetails,name='book_details'),
    path('new_book/',new_book,name="new_book"),
    path('delete_book/,<int:book_id>', delete_book,name="delete_book"),
    path('edit_book/,<int:book_id>', edit_book,name="edit_book")
]




