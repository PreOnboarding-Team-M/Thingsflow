import pytest
from django.urls import reverse
from posts.models import Post

pytestmark = pytest.mark.django_db


def test_post_create_success(client):
    """Post 생성 테스트 - 성공"""
    url = reverse("posts:post-create")
    data = {"title": "제목", "body": "본문", "password": "123abc"}

    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data["title"] == "제목"
    assert response.data["body"] == "본문"


def test_post_update_success(client):
    """Post 수정 테스트 - 성공"""
    post = Post.objects.create(title="제목", body="본문", password="123abc")
    data = {"title": "제목 수정", "body": "본문 수정", "password": "123abc"}
    url = reverse("posts:post-update", kwargs={"pk": post.pk})

    response = client.patch(url, data=data, content_type="application/json")

    assert response.status_code == 200
    assert response.data["title"] == "제목 수정"
    assert response.data["body"] == "본문 수정"


def test_post_list_success_with_only_20_posts(client, sample_posts):
    """Post 목록 조회 테스트 - 성공
    20개의 Post만 조회 -> pagination
    """
    length = len(sample_posts[:20])
    url = reverse("posts:post-list") + "?page=1"

    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data["results"]) == length


def test_post_list_success_with_left_10_posts(client, sample_posts):
    """Post 목록 조회 테스트 - 성공
    10개의 Post만 조회 - pagination
    """
    length = len(sample_posts[20:])
    url = reverse("posts:post-list") + "?page=2"

    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data["results"]) == length
