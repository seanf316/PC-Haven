from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("add/<product_id>/", views.add_to_cart, name="add_to_cart"),
    path("edit/<product_id>/", views.edit_cart, name="edit_cart"),
    path(
        "delete/<product_id>/",
        views.delete_from_cart,
        name="delete_from_cart",
    ),
]
