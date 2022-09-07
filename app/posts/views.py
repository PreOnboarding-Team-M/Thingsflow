from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from posts.serializers import PostSerializer, PostUpdateDeleteSerializer
from posts.models import Post


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by("-id")


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.order_by("-id")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostSerializer
        return PostUpdateDeleteSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return self.destroy(request, *args, **kwargs)
