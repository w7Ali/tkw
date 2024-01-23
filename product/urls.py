# urls.py
from django.urls import path
from .views import add_product, product_detail, top_products, all_product

urlpatterns = [
    path('add/', add_product, name='add-product'),
    path('detail/', all_product, name='all-product'),
    path('detail/<int:pk>/', product_detail, name='product-detail'),
    path('summary/<str:period>/', top_products, name='top-products'),

]



