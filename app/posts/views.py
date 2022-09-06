from rest_framework.generics import CreateAPIView
from posts.serializers import PostSerializer
from posts.models import Post


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
