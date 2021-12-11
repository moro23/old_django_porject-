#blog/urls.py
from django.urls import path

from .views import BlogListView , DetailBlogView , CreateBlogPost , UpdateBlogPost, DeleteBlogPost

urlpatterns =[
    path('post/<int:pk>/delete/', DeleteBlogPost.as_view(), name='delete_post'),
    path('post/<int:pk>/edit/', UpdateBlogPost.as_view(), name='edit_post'),
    path('post/add/', CreateBlogPost.as_view(), name='add_post'),
    path('post/<int:pk>/', DetailBlogView.as_view(), name='detail_page'),
    path('', BlogListView.as_view(), name='home'),
    
]