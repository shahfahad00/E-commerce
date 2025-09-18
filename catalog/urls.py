from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

    # API endpoints
    path('api/products/', views.api_product_list, name='api_product_list'),
    path('api/products/<slug:slug>/', views.api_product_detail, name='api_product_detail'),
]