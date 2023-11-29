from .models import Operating
from .serializers import OperatingSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from branches.permissions import IsLinkedToBranch


class ListCreateOperatingView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLinkedToBranch]
    queryset = Operating.objects.all()
    serializer_class = OperatingSerializer


class RetrieveUpdateDeleteOperatingView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLinkedToBranch]
    queryset = Operating.objects.all()
    serializer_class = OperatingSerializer
