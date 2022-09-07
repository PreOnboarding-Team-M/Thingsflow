from django.urls import path
from posts.views import PostCreateView, PostListView, PostRetrieveUpdateDeleteView


app_name = "posts"

urlpatterns = [
    path("", PostCreateView.as_view(), name="post-create"),
    path("lists/", PostListView.as_view(), name="post-list"),
    path(
        "<int:pk>/",
        PostRetrieveUpdateDeleteView.as_view(),
        name="post-retrieve-update-delete",
    ),
]
