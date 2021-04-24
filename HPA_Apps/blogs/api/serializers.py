from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from HPA_Apps.blogs.models import Post, Comment


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
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
    image = SerializerMethodField()

    class Meta:
        fields = (
            "id",
            "author",
            # "slug",
            "title",
            "body",
            "post_date",
            # "status",
            "image",
        )
        model = Post

    def get_author(
        self,
        obj,
    ):
        return str(obj.author.first_name)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class CommentSerializer(ModelSerializer):
    # reply_count = SerializerMethodField()
    name = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "name",
            # 'parent',
            "body",
            # 'reply_count',
            "date_added",
        ]

    # def get_reply_count(self, obj):
    #     if obj.is_parent:
    #         return obj.children().count()
    #     return 0

    def get_name(
        self,
        obj,
    ):
        return str(obj.name.first_name)
