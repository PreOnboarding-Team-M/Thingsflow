import pytest
from django.urls import reverse
from posts.models import Post
from posts.tests.mocks import create_mock_weather_data

pytestmark = pytest.mark.django_db


def test_post_create_success(client, mocker):
    """Post 생성 테스트 - 성공"""
    url = reverse("posts:post-create")
    mocker.patch("posts.service.get_weather_data", create_mock_weather_data)
    data = {"title": "제목", "body": "본문", "password": "123abc"}

    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data["title"] == "제목"
    assert response.data["body"] == "본문"


def test_post_update_success(client, mocker):
    """Post 수정 테스트 - 성공"""
    mocker.patch("posts.service.get_weather_data", create_mock_weather_data)
    post = Post.objects.create(title="제목", body="본문", password="123abc")
    data = {"title": "제목 수정", "body": "본문 수정", "password": "123abc"}
    url = reverse("posts:post-retrieve-update-delete", kwargs={"pk": post.pk})

    response = client.patch(url, data=data, content_type="application/json")

    assert response.status_code == 200
    assert response.data["title"] == "제목 수정"
    assert response.data["body"] == "본문 수정"


def test_post_update_fail_with_wrong_password(client):
    """Post 수정 테스트 - 실패
    비밀번호 틀림
    """
    post = Post.objects.create(title="제목", body="본문", password="123abc")
    data = {"title": "제목 수정", "body": "본문 수정", "password": "123abcd"}
    url = reverse("posts:post-retrieve-update-delete", kwargs={"pk": post.pk})

    response = client.patch(url, data=data, content_type="application/json")

    assert response.status_code == 400
    assert response.data["password"] == ["비밀번호가 일치하지 않습니다."]


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


def test_post_delete_success(client):
    """Post 삭제 테스트 - 성공"""
    post = Post.objects.create(title="제목", body="본문", password="123abc")
    url = reverse("posts:post-retrieve-update-delete", kwargs={"pk": post.pk})

    response = client.delete(
        url, data={"password": "123abc"}, content_type="application/json"
    )

    assert response.status_code == 204


def test_post_delete_fail_with_wrong_password(client):
    """Post 삭제 테스트 - 실패
    비밀번호 틀림
    """
    post = Post.objects.create(title="제목", body="본문", password="123abc")
    url = reverse("posts:post-retrieve-update-delete", kwargs={"pk": post.pk})

    response = client.delete(
        url, data={"password": "123abcd"}, content_type="application/json"
    )

    assert response.status_code == 400
    assert response.data["password"] == ["비밀번호가 일치하지 않습니다."]
