from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters on the right side of the admin page
    list_filter = ("publication_year", "author")

    # Enable search functionality (search by title and author)
    search_fields = ("title", "author")

    # Optional: ordering of books in admin
    ordering = ("publication_year", "title")



admin.site.register
