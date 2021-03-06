from django.urls import path

from .views import BookListView, BookDetailView

app_name = "books"

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/<slug:slug>', BookDetailView.as_view(), name='book_detail'),
]
