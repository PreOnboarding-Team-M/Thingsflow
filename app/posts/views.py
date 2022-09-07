from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from posts.serializers import PostSerializer, PostUpdateDeleteSerializer
from posts.models import Post


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by("-id")


class PostUpdateView(UpdateAPIView):
    serializer_class = PostUpdateDeleteSerializer
    queryset = Post.objects.order_by("-id")
