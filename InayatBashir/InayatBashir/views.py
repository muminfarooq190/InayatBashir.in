from core.models import Blog, Places
from django.shortcuts import render
from django.http import HttpResponse
def simple(request):
    # blog = Blog.objects.all()
    return render(request, 'index.html')

