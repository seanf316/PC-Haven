from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogs, name="blogs"),
    path("<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path("<int:blog_id>/like/", views.like_blog, name="like_blog"),
]
