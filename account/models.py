from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

__all__ = ["User"]


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name="account_user_set",
        help_text="The groups this user belongs to.",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name="account_user_set",
        help_text="Specific permissions for this user.",
    )
