from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogs, name="blogs"),
    path("add/", views.add_blog, name="add_blog"),
    path("edit/<slug:slug>/", views.edit_blog, name="edit_blog"),
    path("delete/<slug:slug>/", views.delete_blog, name="delete_blog"),
    path("add/comment/<slug:slug>/", views.add_comment, name="add_comment"),
    path(
        "edit/comment/<slug:slug>/<int:comment_id>/",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "delete/comment/<slug:slug>/<int:comment_id>/",
        views.delete_comment,
        name="delete_comment",
    ),
    path("<slug:slug>/like/", views.like_blog, name="like_blog"),
    path("<slug:slug>/", views.blog_detail, name="blog_detail"),
]
