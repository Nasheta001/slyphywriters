from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog_list(request):
    posts = Post.objects.filter(status='published')
    categories = Category.objects.all()
    category_slug = request.GET.get('category')
    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=current_category)
    return render(request, 'blog/blog_list.html', {
        'posts': posts, 'categories': categories, 'current_category': current_category
    })

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    related = Post.objects.filter(status='published', category=post.category).exclude(pk=post.pk)[:3]
    return render(request, 'blog/blog_detail.html', {'post': post, 'related': related})
