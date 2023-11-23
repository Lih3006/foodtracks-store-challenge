from django.urls import path
from .views import ListCreateAccountView, RetrieveUpdateDeleteAccountView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("accounts/", ListCreateAccountView.as_view()),
    path("accounts/<uuid:pk>/", RetrieveUpdateDeleteAccountView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
