from django.urls import path
from .views import CreateCompanyView, RetrieveUpdateDeleteCompanyView

urlpatterns = [
    path("companies/", CreateCompanyView.as_view()),
    path("companies/<uuid:pk>/", RetrieveUpdateDeleteCompanyView.as_view()),
]
