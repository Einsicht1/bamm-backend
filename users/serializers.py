from rest_framework import serializers


class KakaoSocialLoginSerializer(serializers.Serializer):
    code = serializers.CharField()
