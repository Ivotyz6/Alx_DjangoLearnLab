from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# 📌 Function-based view: List all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    # Render an HTML template
    return render(request, 'list_books.html', {'books': books})


# 📌 Class-based view: Display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # template to use
    context_object_name = 'library'        # context name in template

    
