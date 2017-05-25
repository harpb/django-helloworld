from rest_framework import viewsets
from rest_framework.serializers import Serializer, ModelSerializer

from hello.models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = []
    serializer_class = PostSerializer