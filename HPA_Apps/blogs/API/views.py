from rest_framework import generics
from HPA_Apps.blogs.API.serializers import PostListSerializer,PostCreateUpdateSerializer,PostDetailSerializer
from HPA_Apps.blogs.models import Post
from django.db.models import Q
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,)
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
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