from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Blog
from .forms import BlogForm


def blogs(request):
    """A view to show the blogs page"""

    blogs = Blog.objects.all()

    template = "blog/blogs.html"
    context = {
        "blogs": blogs,
    }

    return render(request, template, context)
