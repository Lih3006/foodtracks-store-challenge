from django.urls import path
from .views import ListCreateBranchView, RetrieveUpdateDeleteBranchView

urlpatterns = [
    path("branches/", ListCreateBranchView.as_view()),
    path("branches/<int:pk>/", RetrieveUpdateDeleteBranchView.as_view()),
]
