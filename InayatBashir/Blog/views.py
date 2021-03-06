# Create your views here.
from core.models import Blog, Places
from itertools import chain
from django import template
from django.views.generic import (
        ListView,TemplateView, DetailView
)
from django.shortcuts import render



class ListTopBlogs(ListView):
    template_name = 'Blog/index.html'
    # context_object_name = 'blogs'

    def get_queryset(self):
        
        places = Places.objects.filter(is_in_top_four=True).order_by('date')
        blogs = Blog.objects.filter(is_in_top_three=True).order_by('published_on')

        queryset_chain = chain( places, blogs)
        qs = sorted(queryset_chain, key=lambda instance:instance.pk)
        return qs



class ListAllBlogs(ListView):
    template_name = 'Blog/blogs_list.html'
    context_object_name = 'blogs_list'
   
    def get_queryset(self):
        return Blog.objects.all()


class DetailBlog(DetailView):
    model = Blog
    template_name = 'Blog/blogs_detail.html'
    context_object_name = 'blog'


class AboutMe(TemplateView):
    template_name = 'Blog/about.html'

