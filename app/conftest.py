import pytest
from mixer.backend.django import mixer
from posts.models import Post


@pytest.fixture
def sample_posts():
    """샘플 포스트 데이터 생성"""
    return mixer.cycle(30).blend(Post)
