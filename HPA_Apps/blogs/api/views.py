from rest_framework import generics
from rest_framework.generics import CreateAPIView, get_object_or_404,RetrieveAPIView
from rest_framework.response import Response

from .serializers import (PostListSerializer, PostCreateUpdateSerializer,
                          PostDetailSerializer, CommentListSerializer,CommentSerializer,
                          create_comment_serializer)
from ..models import Post,Comment
from django.db.models import Q
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,)
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
 )


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostApiListView(generics.ListCreateAPIView):
    serializer_class = PostListSerializer
    search_fields = ['title', 'content', 'user__first_name']
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__first_name__icontains=query) |
               Q(author__last_name__icontains=query)
            ).distinct()
        return queryset_list


class PostApiDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    #lookup_field = 'slug'
    permission_classes = [AllowAny]


class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    #lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]


#comment Api

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()



    def get_serializer_class(self):
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comment_serializer(
                slug=slug,
                parent_id=parent_id,
                author=self.request.user
                )


class CommentApiListView(generics.ListCreateAPIView):
    serializer_class = CommentListSerializer
    search_fields = ['content', 'author_first_name']
    filter_backends = [SearchFilter, OrderingFilter]
    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(author__first_name__icontains=query) |
               Q(author__last_name__icontains=query)
            ).distinct()
        return queryset_list


class CommentDetaliAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # lookup_field = 'id'


