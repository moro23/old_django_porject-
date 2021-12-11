from django.views.generic import ListView , DetailView

from .models import Book

# Create your views here.
class BookListView(ListView):
    queryset = Book.objects.all()
    context_name = "book_list"
    #paginate_by = 3
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    queryset = Book.objects.all()
    #model = Book
    context_name = 'book'
    template_name = 'books/book_detail.html'