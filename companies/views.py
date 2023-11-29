# from rest_framework.views import APIView, Request, Response, status
from .models import Company
from .serializers import CompanySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAdminAndAccountOwner
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema

class ListCreateCompanyView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminAndAccountOwner]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Company.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDeleteCompanyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminAndAccountOwner]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @extend_schema(
        operation_id='company_put', exclude=True,
        summary='Update all fields from Company',
        description='Update all fields from Company',
    )
    def put(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)