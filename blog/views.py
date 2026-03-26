from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Article
from .forms import ArticleForm


@login_required
def article_list(request):
    articles = Article.objects.filter(published=True)
    return render(request, 'blog/article_list.html', {'articles': articles})


@permission_required('blog.add_article', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Artículo creado.')
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})


@login_required
@permission_required('blog.delete_article', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Artículo eliminado.')
        return redirect('article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})


@permission_required('blog.publish_article', raise_exception=True)
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.published = True
    article.save()
    messages.success(request, f'"{article.title}" ha sido publicado.')
    return redirect('article_list')