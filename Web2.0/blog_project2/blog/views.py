from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'list_all_post'

class DetailBlogView(DetailView):
    model = Post
    template_name = 'detail_page.html'

class CreateBlogPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

class UpdateBlogPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

class DeleteBlogPost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')