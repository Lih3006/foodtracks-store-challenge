from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    branch_state = models.CharField(max_length=30)
    branch_city = models.CharField(max_length=50)
    branches = models.ManyToManyField(
        "branches.Branch", related_name="accounts", default=""
    )
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=14)

    def __repr__(self) -> str:
        return f"<Account: {self.username}>"
