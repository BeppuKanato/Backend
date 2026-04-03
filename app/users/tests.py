import uuid
from django.test import TestCase
from django.urls import reverse
from .models import User, Token


class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse("user-registration"))

        self.assertEqual(response.status_code, 201)

        data = response.json()
        self.assertIn("userId", data)  # userIdがレスポンスに含まれていることを確認
        self.assertIn(
            "accessToken", data
        )  # accessTokenがレスポンスに含まれていることを確認

        self.assertTrue(data["userId"])  # userIdが空でないことを確認
        self.assertEqual(
            len(data["accessToken"]), 64
        )  # accessTokenが64文字であることを確認

        uuid.UUID(data["userId"], version=4)  # userIdがUUIDv4形式であることを確認

        self.assertEqual(
            User.objects.count(), 1
        )  # ユーザーが1件作成されていることを確認
        self.assertEqual(
            Token.objects.count(), 1
        )  # トークンが1件作成されていることを確認

        user = User.objects.get()
        token = Token.objects.get()

        self.assertEqual(
            user.user_id, data["userId"]
        )  # ユーザーIDがレスポンスのuserIdと一致することを確認
        self.assertEqual(
            token.token, data["accessToken"]
        )  # トークンがレスポンスのaccessTokenと一致することを確認
        self.assertEqual(
            token.user, user
        )  # トークンのユーザーが作成されたユーザーと一致することを確認

        self.assertEqual(user.crystal, 0)  # ユーザーのcrystalが0であることを確認
        self.assertEqual(
            user.crystal_free, 0
        )  # ユーザーのcrystal_freeが0であることを確認
        self.assertEqual(
            user.friend_coin, 0
        )  # ユーザーのfriend_coinが0であることを確認
        self.assertEqual(
            user.tutorial_progress, 0
        )  # ユーザーのtutorial_progressが0であることを
