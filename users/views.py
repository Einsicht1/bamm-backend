from django.conf import settings
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from users.serializers import KakaoSocialLoginSerializer
from users.services.kakao_service import kakao_service


class KakakoSocialLoginAPIVIew(GenericAPIView):
    serializer_class = KakaoSocialLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email, jwt_token = kakao_service.login(code=serializer.validated_data["code"])
        response = Response(email)
        response.set_cookie(
            "access_token",
            jwt_token["access"],
            httponly=True,
            max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            secure=True,
            domain="bamm.kr",
        )
        return response
