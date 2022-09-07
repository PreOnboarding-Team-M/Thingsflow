import pytest
from django.db.utils import DataError
from django.contrib.auth.hashers import check_password
from posts.models import Post

pytestmark = pytest.mark.django_db


def test_post_model_create_success():
    """Post 모델 생성 테스트 - 성공"""
    post = Post.objects.create(title="제목", body="본문", password="102938")

    assert post.title == "제목"
    assert post.body == "본문"
    assert check_password("102938", post.password)


def test_post_model_create_fail_with_long_title():
    """
    Post 모델 생성 테스트 - 실패
    제목 20자 초과
    """
    with pytest.raises(DataError):
        Post.objects.create(title="제목" * 50, body="본문", password="123abc")


def test_post_model_create_fail_with_long_body():
    """
    Post 모델 생성 테스트 - 실패
    본문 200자 초과
    """
    with pytest.raises(DataError):
        Post.objects.create(title="제목", body="본문" * 101, password="123abc")


def test_post_model_create_success_with_emoji():
    """Post 모델 생성 테스트 - 성공
    이모지 포함
    """
    post = Post.objects.create(title="제목", body="본문😀", password="102938")

    assert post.title == "제목"
    assert post.body == "본문😀"
    assert check_password("102938", post.password)
