from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.groups.all()[:settings.NUM_POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)


def index(request):
    posts = Post.objects.all()[:settings.NUM_POSTS_ON_PAGE]
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)
