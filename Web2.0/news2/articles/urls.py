#articles/urls.py
from django.urls import path

from .views import (

    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView, 
    ArticleCreateView,
    CreateCommentView,
   

)

urlpatterns = [
    path('addcomment/', CreateCommentView.as_view(), name='article_comment'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
]