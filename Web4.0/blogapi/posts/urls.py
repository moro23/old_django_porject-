#posts/url.py 
from django.urls import path

from .views import ListPost, DetailPost, UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/',DetailPost.as_view()),
    path('', ListPost.as_view()),
]