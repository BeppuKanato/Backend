from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=36, primary_key=True)
    user_name = models.CharField(max_length=15, null=True, blank=True)
    crystal = models.IntegerField(default=0)
    crystal_free = models.IntegerField(default=0)
    friend_coin = models.IntegerField(default=0)
    tutorial_progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
    
    def __str__(self) -> str:
        return self.user_id

class Token(models.Model):
    token_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="tokens",
    )
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    class Meta:
        db_table = "tokens"
    
    def __str__(self) -> str:
        return self.token[:10]
