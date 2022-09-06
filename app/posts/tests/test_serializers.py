import pytest
from rest_framework import serializers
from posts.serializers import PostSerializer


pytestmark = pytest.mark.django_db


def test_post_serializer_create_success():
    """PostSerializer 생성 테스트 - 성공"""

    data = {"title": "제목", "body": "본문", "password": "123abc"}

    serializer = PostSerializer(**data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    assert serializer.data["title"] == "제목"
    assert serializer.data["body"] == "본문"
    assert serializer.data["password"] == "123abc"


def test_post_serializer_create_fail_with_short_password():
    """PostSerializer 생성 테스트 - 실패
    비밀번호 6자 미만
    """
    data = {"title": "제목", "body": "본문", "password": "123ab"}

    serializer = PostSerializer(**data)

    with pytest.raises(serializers.ValidationError):
        serializer.is_valid(raise_exception=True)
        serializer.save()


def test_post_serializer_create_fail_with_no_digit_password():
    """PostSerializer 생성 테스트 - 실패
    비밀번호 숫자 미포함
    """
    data = {"title": "제목", "body": "본문", "password": "abcdef"}

    serializer = PostSerializer(**data)

    with pytest.raises(serializers.ValidationError):
        serializer.is_valid(raise_exception=True)
        serializer.save()
