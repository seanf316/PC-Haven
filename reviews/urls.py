from django.urls import path
from . import views

urlpatterns = [
    path(
        "add_review/<slug:slug>/",
        views.add_review,
        name="add_review",
    ),
    path(
        "edit_review/<slug:slug>/<int:review_id>/",
        views.edit_review,
        name="edit_review",
    ),
    path(
        "delete_review/<slug:slug>/<int:review_id>/",
        views.delete_review,
        name="delete_review",
    ),
]
