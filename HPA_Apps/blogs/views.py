from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import Post, Category, Comment

# Create your views here.


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    # fields = '__all__'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("blogs:post_detail", args=[str(pk)]))
    # return HttpResponseRedirect(reverse("home"))


class BlogListView(ListView):
    model = Post
    template_name = "posts.html"
    # cats = Category.objects.all()
    ordering = ["-id"]

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    return render(
        request,
        "categories.html",
        {"cats": cats.title().replace("-", " "), "category_posts": category_posts},
    )


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)

        thing = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = thing.total_likes()

        liked = False
        if thing.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_new.html"
    # fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "post_edit.html"
    # fields = ['title','body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


class CategoryCreateView(CreateView):
    model = Category
    template_name = "category_new.html"
    fields = "__all__"
