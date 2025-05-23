from django.urls import path
from form.views import (
    main_view,
    add_product_view,
    product_view,
    product_edit,
    product_delete
)

urlpatterns = [
    path('', main_view, name='main'),
    path('add-product/', add_product_view, name='add-product'),
    path('products/', product_view, name='product-list'),
    path('products/<int:pk>/edit/', product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
]
