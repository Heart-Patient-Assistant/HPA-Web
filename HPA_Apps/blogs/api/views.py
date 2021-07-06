from rest_framework import generics
from rest_framework import viewsets, permissions
from .serializers import (
    CommentSerializer,
    PostListSerializer,
    PostCreateUpdateSerializer,
    PostDetailSerializer,
)
from .. import models
from ..models import Post, Comment
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from django.shortcuts import get_object_or_404


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostApiListView(generics.ListCreateAPIView):
    serializer_class = PostListSerializer
    search_fields = ["title", "content", "user__first_name"]
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(author__first_name__icontains=query)
                | Q(author__last_name__icontains=query)
            ).distinct()
        return queryset_list


class PostApiDetailView(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    permission_classes = [AllowAny]

    @action(detail=False, methods=["POST", "GET"])
    def comments(self, request, pk):
        # get_object_or_404(Comment, pk=comment_id)
        post = get_object_or_404(Post, pk=pk)
        if request.method == "GET":
            self.serializer_class = CommentSerializer
            if models.Comment.objects.filter(post=post):
                queryset = models.Comment.objects.filter(post=post)
                serializer = CommentSerializer(
                    queryset, many=True, context={"request": request}
                )
                return Response(serializer.data)
            else:
                return Response({"message": "There is no comment"})
        else:
            self.serializer_class = CommentSerializer
            queryset = models.Comment.objects.filter(post=post)
            serializer = CommentSerializer(
                data=request.data, context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(author=self.request.user, post=post)
            return Response(serializer.data)

    @action(detail=False, methods=["DELETE"])
    def remove_comment(self, request, pk, comment):
        comment = get_object_or_404(Comment, pk=comment)
        if comment.delete():
            return Response({"message": "Comment deleted"})
        else:
            return Response({"message": "unable to delete comment"})


class postlist(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    permission_classes = [AllowAny]


class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    # lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]
