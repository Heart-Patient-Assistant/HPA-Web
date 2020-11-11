
from .models import Post
#from HPA_Apps.blogs.api.serializers import
from django.views.generic import CreateView






class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = '__all__'
