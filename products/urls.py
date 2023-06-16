from django.urls import path
from . import views

urlpatterns = [
    path("", views.allproducts, name="products"),
    path("add/", views.add_product, name="add_product"),
    path("<slug:slug>/", views.product_detail, name="product_detail"),
    path("edit/<slug:slug>/", views.edit_product, name="edit_product"),
    path("delete/<slug:slug>/", views.delete_product, name="delete_product"),
]
