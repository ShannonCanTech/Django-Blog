from django.shortcuts import render
from django.utils import timezone
from .models import Post  # The dot means current directory/application

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  #Retrieves QuerySet by published date
    return render(request, 'blog/post_list.html', {'posts': posts})