from django.urls import path


from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug:category_slug>/', views.homepage, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]

