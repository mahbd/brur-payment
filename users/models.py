from django.contrib.auth.models import AbstractUser
from django.db import models

from constants import DEPARTMENTS


class User(AbstractUser):
    department = models.CharField(max_length=127, choices=DEPARTMENTS, blank=True, null=True)
