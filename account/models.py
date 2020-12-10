from django.db import models
from django.contrib.auth.models import User
from questions.models import Category


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="نام کاربر"
    )
    GENDER_CHOICES = (("male", "مرد"), ("female", "زن"))
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        verbose_name="جنسیت",
        null=True,
        blank=True,
    )
    interests = models.ManyToManyField(Category, verbose_name="علاقه مندی ها", blank=True)
    avatar = models.ImageField(
        upload_to="user/%Y/%m/%d", verbose_name="آواتار", null=True, blank=True
    )

    class Meta:
        db_table = "profile"
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"

    def __str__(self):
        return f"Profile for user {self.user.username}"
