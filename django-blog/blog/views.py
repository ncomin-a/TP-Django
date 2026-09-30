from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from blog.forms import CommentForm
from blog.models import Post, Comment


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    return render(request, "blog/index.html", {"posts": posts})


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__iexact=category
    ).order_by("-created_on")
    context = {"category": category, "posts": posts}
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post).order_by("-created_on")
    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog/detail.html", context)
