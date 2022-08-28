from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Страница c постами, отфильтрованными по группам.
def group_posts(request, slug):
    title = 'Записи сообщества'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)


def index(request):
    title = 'Последние обновления на сайте'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


