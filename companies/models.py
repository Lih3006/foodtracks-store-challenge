from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=60)
    owner = models.OneToOneField(
        "accounts.Account", on_delete=models.CASCADE, related_name="company"
    )
