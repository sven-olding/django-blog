from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    paginator = Paginator(Post.published.all(), 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.get_page(page_number)
    except EmptyPage:
        # If the page number is invalid return the last page.
        posts = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        # If the page number is not an integer, return the first page.
        posts = paginator.get_page(1)
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )
    return render(request, "blog/post/detail.html", {"post": post})
