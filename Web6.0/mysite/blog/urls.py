from django.urls import path
from . import views 
#from .views import PostListView, PostDetaiViewl, post_share

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<uuid:post_id>/share/', views.post_share, name='post_share'),
    path('search/', views.post_search, name='post_search'),
]