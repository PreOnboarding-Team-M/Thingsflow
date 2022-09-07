from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("apis/posts/", include("posts.urls")),
    path("apis/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "apis/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]
