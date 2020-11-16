from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
    )
from HPA_Apps.blogs.models import Post,Comment
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','slug', 'content', 'created','status','image')


class PostListSerializer(ModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'author',
            'slug',
            'title',
            'publish',
        ]
    def get_author (self, obj,):
        return str(obj.author.first_name)










# Comments serializers
def create_comment_serializer(model_type='post', slug=None, parent_id=None, user=None):
    class CommentCreateSerializer(ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                'object_id',
                'content',
                'created',
                'author',
            ]

        def create(self, validated_data):
            content = validated_data.get("content")
            author = self.context['request'].author
            reply = validated_data['reply']
            slug = self.slug
            parent_obj = self.parent_obj
            comment = Comment.objects.create_by_model_type(
                   slug, content, author,
                    parent_obj=parent_obj,
                    )
            return comment

    return CommentCreateSerializer

















class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'object_id',
            'post',
            'parent',
            'content',
            'reply_count',
            'created',
        ]
    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

class CommentChildSerializer(ModelSerializer):
    reply_count=SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'object_id',
            'author',
            'content',
            ' created',
            'reply_count',
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0




class CommentListSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'object_id',
            'parent',
            'content',
            'reply_count',
            'created',
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0




class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    image = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        fields = ('id', 'author','slug', 'title', 'content', 'created','status','image','comments')
        model = Post


    def get_author (self, obj,):
        return str(obj.author.first_name)


    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):

            c_qs = Comment.objects.filter_by_instance(obj)
            comments = CommentSerializer(c_qs, many=True).data
            return comments
            return None





