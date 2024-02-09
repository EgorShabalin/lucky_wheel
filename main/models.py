from django.db import models
from custom_user.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    current_user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    ava = models.ImageField(default=None, upload_to="avatars", blank=True, null=True)
    balance = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.current_user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(current_user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Wheel(models.Model):
    wheel_list = [
        "10",
        "20",
        "tripple",
        "100",
        "200",
        "double",
        "60",
        "free",
        "90",
        "jackpot",
        "10",
        "30",
        "free",
        "500",
        "1000",
        "broke",
    ]
    percentage = [
        2,
        4,
        4,
        4,
        4,
        4,
        3,
        3,
        6,
        6,
        10,
        10,
        10,
        10,
        10,
        10,
    ]

    def __str__(self) -> str:
        return self.wheel_list
