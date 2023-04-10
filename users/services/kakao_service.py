import requests
from django.contrib.auth import get_user_model

from users.models import User
from users.services.jwt_service import jwt_service


class KakaoService:
    def login(self, code: str) -> (str, dict):
        user_data = self._get_user_data(code)
        try:
            user = get_user_model().objects.get(email=user_data.get("email"))
        except User.DoesNotExist:
            user = get_user_model().objects.create_social_login_user(
                email=user_data["email"],
                social_login_id=user_data.get("kakao_id"),
            )
        return user.email, jwt_service.get_tokens_for_user(user)

    def _get_user_data(self, code: str) -> dict:
        token_data = self._get_token_data(code)
        kakao_user_info_url = "https://kapi.kakao.com/v2/user/me"
        headers = {"Authorization": f"Bearer {token_data['access_token']}"}

        res = requests.post(url=kakao_user_info_url, headers=headers)
        res.json().get("id")

        kakao_id = res.json().get("id")
        connected_at = res.json().get("connected_at")
        properties = res.json().get("properties")
        kakao_account = res.json().get("kakao_account")
        profile_nickname_needs_agreement = kakao_account.get(
            "profile_nickname_needs_agreement"
        )
        profile = kakao_account.get("profile")
        nickname = profile.get("nickname")
        thumbnail = profile.get("thumbnail")
        profile_image_url = profile.get("profile_image_url")
        is_default_image = profile.get("is_default_image")
        has_email = kakao_account.get("has_email")
        email_needs_agreement = kakao_account.get("email_needs_agreement")
        is_email_valid = kakao_account.get("is_email_valid")
        is_email_verified = kakao_account.get("is_email_verified")
        email = kakao_account.get("email")

        return {
            "kakao_id": kakao_id,
            "connected_at": connected_at,
            "properties": properties,
            "kakao_account": kakao_account,
            "profile_nickname_needs_agreement": profile_nickname_needs_agreement,
            "profile": profile,
            "nickname": nickname,
            "thumbnail": thumbnail,
            "profile_image_url": profile_image_url,
            "is_default_image": is_default_image,
            "has_email": has_email,
            "email_needs_agreement": email_needs_agreement,
            "is_email_valid": is_email_valid,
            "is_email_verified": is_email_verified,
            "email": email,
        }

    def _get_token_data(self, code: str) -> dict:
        kakao_auth_base_url = "https://kauth.kakao.com"
        kakao_token_path = "/oauth/token"
        url = f"{kakao_auth_base_url}{kakao_token_path}"
        params = {
            "grant_type": "authorization_code",
            "client_id": "ce2597af0b15d899f76bc01cd6b5b8e2",
            "redirect_uri": "https://bamm.kr/login/oauth/kakao",
            "code": code,
        }
        res = requests.post(url=url, data=params)
        return {
            "access_token": res.json().get("access_token"),
            "token_type": res.json().get("token_type"),
            "refresh_token": res.json().get("refresh_token"),
            "id_token": res.json().get("id_token"),
            "expires_in": res.json().get("expires_in"),
            "scope": res.json().get("scope"),
            "refresh_token_expires_in": res.json().get("refresh_token_expires_in"),
        }


kakao_service = KakaoService()
