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


def blog_detail(request, blog_id):
    """A view to show blog details"""

    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    liked = False

    if user.is_authenticated:
        if blog.likes.filter(id=user.id).exists():
            liked = True

    context = {
        "blog": blog,
        "liked": liked,
    }

    return render(request, "blog/blog_detail.html", context)


def like_blog(request, blog_id):
    """A view to handle liking/unliking on a blog post"""

    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)

    if user.is_authenticated:
        if blog.likes.filter(id=user.id).exists():
            blog.likes.remove(user)
            messages.success(
                request, f"{user} you have unliked this Blog post."
            )
        else:
            blog.likes.add(user)
            messages.success(request, f"{user} you have liked this Blog post.")
    else:
        messages.info(
            request, "Only registered users can like this Blog post."
        )

    return redirect(reverse("blog_detail", args=[blog.id]))
