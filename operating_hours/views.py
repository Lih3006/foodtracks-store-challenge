from rest_framework.views import APIView, Request, Response, status
from .models import Operating
from .serializers import OperatingSerializer

# from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from branches.permissions import IsStateManager, IsCityManager, IsSiteManager


class ListCreateOperatingView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Operating.objects.all()
    serializer_class = OperatingSerializer

    def perform_create(self, serializer):
        print("Aqui", self)
        serializer.save()


class RetrieveUpdateDeleteOperatingView(RetrieveUpdateDestroyAPIView):
    queryset = Operating.objects.all()
    serializer_class = OperatingSerializer
