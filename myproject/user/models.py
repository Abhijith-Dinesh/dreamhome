from django.db import models

class User(models.Model):
    yourname=models.CharField(
        max_length=20,
    )
    youremail=models.EmailField(
        max_length=20,
        unique=True,
        blank=False,
        null=False
    )
    phonenumber=models.BigIntegerField(
        unique=True,
        blank=False,
        null=False
    )
    password=models.CharField(
        max_length=20
    )
    date_joined=models.DateTimeField(
        auto_now_add=True
    )
    update_at=models.DateTimeField(
        auto_now=True
    )
    is_active=models.BooleanField(
        default=True
    )
    def __str__(self):
        return self.yourname
    




