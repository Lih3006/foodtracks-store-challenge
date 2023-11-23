from django.db import models
import uuid


class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    company_name = models.CharField(max_length=60)
    owner = models.OneToOneField(
        "accounts.Account", on_delete=models.CASCADE, related_name="company"
    )
