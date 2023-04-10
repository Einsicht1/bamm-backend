from dataclasses import dataclass


@dataclass
class KakaoUserProfile:
    kakao_id: str
    connected_at: str
    properties: str
    kakao_account: str
    profile_nickname_needs_agreement: str
    profile: str
    nickname: str
    thumbnail: str
    profile_image_url: str
    is_default_image: str
    has_email: str
    email_needs_agreement: str
    is_email_valid: str
    is_email_verified: str
    email: str
