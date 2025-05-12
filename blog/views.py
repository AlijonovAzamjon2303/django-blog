from django.http import HttpResponse
from .models import Post
from django.shortcuts import render

# Create your views here.
def home(request):
    posts = Post.objects.all()
    post_titles = ", ".join([post.title for post in posts])

    return HttpResponse(f"Blog posts : {post_titles}")