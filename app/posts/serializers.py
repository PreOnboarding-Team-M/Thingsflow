from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("비밀번호는 6자 이상이어야 합니다.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("비밀번호는 숫자를 포함해야 합니다.")
        return value


class PostUpdateDeleteSerializer(PostSerializer):
    def validate_password(self, value):
        if not check_password(value, self.instance.password):
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return value
