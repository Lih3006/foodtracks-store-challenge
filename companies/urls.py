from django.urls import path
from .views import ListCreateCompanyView, RetrieveUpdateDeleteCompanyView

urlpatterns = [
    path("companies/", ListCreateCompanyView.as_view()),
    path("companies/<uuid:pk>/", RetrieveUpdateDeleteCompanyView.as_view()),
]
