import pytest
from mixer.backend.django import mixer
from posts.models import Post
from posts.tests.mocks import create_mock_weather_data


@pytest.fixture
def sample_posts(mocker):
    """샘플 포스트 데이터 생성"""
    mocker.patch("posts.service.get_weather_data", create_mock_weather_data)
    return mixer.cycle(30).blend(Post)
