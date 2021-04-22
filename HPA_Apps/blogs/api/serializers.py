from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
    )
from rest_framework import serializers
from HPA_Apps.blogs.models import Post,Comment



class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title',
                  # 'slug',
                  'content', 'created','status','image')


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'author',
            # 'slug',
            'title',
            'publish',
            'content'
        ]
    def get_author (self, obj,):
        return str(obj.author.first_name)

class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        fields = ('id', 'author','slug', 'title', 'content', 'created','status','image')
        model = Post


    def get_author (self, obj,):
        return str(obj.author.first_name)


    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image



class CommentSerializer(ModelSerializer):
    # reply_count = SerializerMethodField()
    author = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            # 'parent',
            'body',
            # 'reply_count',
            'created',
        ]
    # def get_reply_count(self, obj):
    #     if obj.is_parent:
    #         return obj.children().count()
    #     return 0

    def get_author (self, obj,):
        return str(obj.author.first_name)







