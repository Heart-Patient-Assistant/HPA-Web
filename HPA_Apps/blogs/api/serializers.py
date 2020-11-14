from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
    )
from HPA_Apps.blogs.models import Post



class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title','slug', 'content', 'created','status','image')


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





