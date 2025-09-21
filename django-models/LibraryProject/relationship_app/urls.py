from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based view to list all books
    path('books/', list_books, name='list_books'),

    # Class-based view to display a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
