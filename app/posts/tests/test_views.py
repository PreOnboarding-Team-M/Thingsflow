import pytest
from django.urls import reverse


pytestmark = pytest.mark.django_db


def test_post_create_success(client):
    """Post 생성 테스트 - 성공"""
    url = reverse("posts:post-create")
    data = {"title": "제목", "body": "본문", "password": "123abc"}

    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data["title"] == "제목"
    assert response.data["body"] == "본문"
