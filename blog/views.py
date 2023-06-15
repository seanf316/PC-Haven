from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Blog, Comment
from .forms import BlogForm, CommentForm


def blogs(request):
    """A view to show the blogs page"""

    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page = request.GET.get("page")
    paginated_blogs = paginator.get_page(page)

    template = "blog/blogs.html"
    context = {
        "blogs": paginated_blogs,
    }

    return render(request, template, context)


def blog_detail(request, blog_id):
    """A view to show blog details"""

    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    liked = False
    comments = Comment.objects.filter(blog=blog).order_by("-created_on")

    if user.is_authenticated:
        if blog.likes.filter(id=user.id).exists():
            liked = True

    context = {
        "blog": blog,
        "liked": liked,
        "comments": comments,
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


@login_required()
def add_blog(request):
    """Add a blog post to the site"""

    user = request.user

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    if user.is_superuser:
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = user
                blog.save()
                title = form.cleaned_data["title"]
                messages.success(
                    request, f"Successfully added blog post - {title}."
                )
                return redirect(reverse("blogs"))
            else:
                messages.error(
                    request,
                    (
                        "Failed to add blog post. "
                        "Please ensure the form is valid."
                    ),
                )
        else:
            form = BlogForm()
    else:
        messages.error(request, "You are not authorized to add a Blog post.")
        return redirect(reverse("blogs"))

    template = "blog/add_blog.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """Edit a blog post"""
    user = request.user

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("home"))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = user
            blog.save()
            title = form.cleaned_data["title"]
            messages.success(
                request, f"Successfully updated blog post - {title}."
            )
            return redirect(reverse("blog_detail", args=[blog.id]))
        else:
            messages.error(
                request,
                (
                    "Failed to add blog post. "
                    "Please ensure the form is valid."
                ),
            )
    else:
        form = BlogForm(instance=blog)
        messages.info(
            request,
            f"{user.username} you are editing Blog post - {blog.title}",
        )

    template = "blog/edit_blog.html"
    context = {
        "form": form,
        "blog": blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """Delete a blog post"""
    user = request.user

    if not user.is_superuser:
        messages.error(
            request, f"Sorry {user.username}, only store owners can do that."
        )
        return redirect(reverse("blogs"))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, f"Blog post {blog.title} has been deleted!")
    return redirect(reverse("blogs"))


def add_comment(request, blog_id):
    """
    Function to comment on existing blogs
    """
    blog = get_object_or_404(Blog, pk=blog_id)

    if not request.user.is_authenticated:
        messages.info(
            request,
            "You will need to Sign Up or Login to add comments to the Blog Post.",
        )
        return redirect(reverse("blog_detail", args=[blog.id]))

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog  # Set the blog field
            comment.name = (
                request.user
            )  # Set the name field to the current user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect(reverse("blog_detail", args=[blog.id]))
        else:
            messages.error(
                request,
                "Failed to add blog comment. Please ensure the form is valid.",
            )
    else:
        form = CommentForm()

    context = {
        "form": form,
        "blog": blog,
    }

    return render(request, "blog/add_comment.html", context)


@login_required()
def edit_comment(request, blog_id, comment_id):
    """
    Checks the database for the comment.id and then confirms if
    user matches the comment user before allowing user to edit their comment
    """
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if user.is_superuser or user == comment.name:
        if request.method == "POST":
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.save()
                messages.success(
                    request, f"{user.username} your comment has been updated"
                )

                return redirect(reverse("blog_detail", args=[blog.id]))
            else:
                messages.error(
                    request,
                    "Comment updated failed, please review the form.",
                )
        else:
            form = CommentForm(instance=comment)

    else:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect(reverse("blog_detail", args=[blog.id]))

    context = {
        "form": form,
        "blog": blog,
        "comment": comment,
    }

    return render(request, "blog/edit_comment.html", context)


@login_required
def delete_comment(request, blog_id, comment_id):
    """Delete a comment from the blog posts"""
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if not user.is_superuser or user != comment.name:
        messages.error(
            request,
            f"Sorry {user.username}, only the staff or owner of the comment can delete.",
        )
        return redirect(reverse("blog_detail", args=[blog.id]))

    comment.delete()
    messages.success(request, f"Comment has been deleted!")
    return redirect(reverse("blog_detail", args=[blog.id]))
