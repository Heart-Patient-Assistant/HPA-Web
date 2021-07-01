from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from HPA_Apps.blogs.models import Post, Comment


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            # "author",
            "title",
            # 'slug',
            "body",
            # "post_date",
            # "status",
            # "image",
        )


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            "author",
            # 'slug',
            "title",
            "post_date",
            "body",
        ]

    def get_author(
        self,
        obj,
    ):
        return str(obj.author.first_name)


class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    header_image = SerializerMethodField()

    class Meta:
        fields = (
            "id",
            "author",
            # "slug",
            "title",
            "body",
            "post_date",
            # "status",
            "header_image",
        )
        model = Post

    def get_author(
        self,
        obj,
    ):
        return str(obj.author.first_name)

    def get_header_image(self, obj):
        try:
            image = obj.header_image.url
        except:
            image = None
        return image


class CommentSerializer(ModelSerializer):
    # reply_count = SerializerMethodField()
    author = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            # 'parent',
            "body",
            # 'reply_count',
            "date_added",
        ]

    # def get_reply_count(self, obj):
    #     if obj.is_parent:
    #         return obj.children().count()
    #     return 0

    def get_author(
        self,
        obj,
    ):
        return str(obj.author.first_name)
