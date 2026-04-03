import secrets
import uuid
from datetime import timedelta

from django.db import transaction
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
from django.shortcuts import render

from .models import User, Token

class UserRegistrationView(View):
    def post(self, request):
        expire_date = 7  # トークンの有効期限（日数）
        try:
            new_user_id = str(uuid.uuid4())
            # 64文字
            access_token = secrets.token_hex(32)
            expired_at = timezone.now() + timedelta(days=expire_date)
            
            with transaction.atomic():
                user = User.objects.create(
                    user_id=new_user_id,
                    user_name=None,
                    crystal=0,
                    crystal_free=0,
                    friend_coin=0,
                    tutorial_progress=0,
                )

                Token.objects.create(
                    user=user,
                    token=access_token,
                    expired_at=expired_at,
                )
            
            return JsonResponse({
                "userId": user.user_id,
                "accessToken": access_token
            }, status=201)

        except Exception as e:
            return JsonResponse({
                "errorCode": "SERVER-001",
                "message": "Internal server error"
            }, status=500)