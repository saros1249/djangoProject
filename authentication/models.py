from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MALE = "m"
    FEMALE = "f"
    SEX = [(MALE, "Male"), (FEMALE, "Female")]

    HR = "hr"
    SEEKER = "seeker"
    UNKNOWN = "unknown"
    ROLE = [(HR, HR), (SEEKER, SEEKER), (UNKNOWN, UNKNOWN)]

    sex = models.CharField(max_length=1, choices=SEX, default=MALE)
    role = models.CharField(max_length=7, choices=ROLE, default=UNKNOWN)
