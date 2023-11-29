from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Account(AbstractUser):
    ROLES = (
        ("owner", "owner"),
        ("regional_manager", "regional_manager"),
        ("site_manager", "site_manager"),
        ("site_employer", "site_employer"),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=14)
    role = models.CharField(max_length=20, choices=ROLES)

    branches = models.ManyToManyField(
        "branches.Branch", related_name="accounts", default=""
    )

    def __repr__(self) -> str:
        return f"<Account: {self.username}>"
