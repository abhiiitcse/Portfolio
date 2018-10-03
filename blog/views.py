from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def all_blogs(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/index.html', {'posts':posts})

def blog_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/blog_detail.html', {'post': post})