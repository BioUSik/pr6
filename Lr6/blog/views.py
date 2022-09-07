from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'new_blog.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body']
    template_name = 'blog_edit.html'

class BlogDeleteView(DeleteView):
    model = Blog
