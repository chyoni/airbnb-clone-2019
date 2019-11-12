# 기본 django가 제공하는 admin 패널에 있는 user가 AbstractUser 임
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    bio = models.TextField(default="")

