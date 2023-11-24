from django.urls import path
from .views import ListCreateBranchView, RetrieveUpdateDeleteBranchView

urlpatterns = [
    path("branches/", ListCreateBranchView.as_view()),
    path("branches/<uuid:pk>/", RetrieveUpdateDeleteBranchView.as_view()),
]
