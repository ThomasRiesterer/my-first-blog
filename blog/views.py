from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts_reversed = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = posts_reversed.reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})