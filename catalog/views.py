from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


# Function view
def index(request):
    """View function for home page."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_books_w_z = Book.objects.filter(title__contains='z').count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_w_z': num_books_w_z,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


# Class view
class BookListView(generic.ListView):
    model = Book
