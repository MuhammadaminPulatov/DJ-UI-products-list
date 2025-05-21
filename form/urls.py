from tkinter.font import names

from django.contrib import admin
from django.urls import path

from form.views import main_view, add_product_view

urlpatterns = [
    path('', main_view),
    path('add-product',add_product_view,name='add-product')
]
