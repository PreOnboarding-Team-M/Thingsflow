from django.urls import path
from posts.views import PostCreateView, PostListView, PostUpdateView


app_name = "posts"

urlpatterns = [
    path("", PostCreateView.as_view(), name="post-create"),
    path("lists/", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostUpdateView.as_view(), name="post-update"),
]
