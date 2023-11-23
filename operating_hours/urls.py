from django.urls import path
from .views import ListCreateOperatingView, RetrieveUpdateDeleteOperatingView

urlpatterns = [
    path("operating_hours/", ListCreateOperatingView.as_view()),
    path(
        "operating_hours/<uuid:branchId>", RetrieveUpdateDeleteOperatingView.as_view()
    ),
]
