from django.db import models


class Branch(models.Model):
    store_name = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=5)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15)
    company = models.ForeignKey(
        "companies.Company", on_delete=models.CASCADE, related_name="branches_company"
    )
    operating_hours = models.ManyToManyField(
        "operating_hours.Operating", related_name="branches"
    )

    def __repr__(self) -> str:
        return f"<Store: {self.store_name} Id: {self.id}>"
