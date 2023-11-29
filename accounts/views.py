from .models import Account
from .serializers import AccountSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrAccountOwner
from drf_spectacular.utils import extend_schema


class ListCreateAccountView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAccountOwner]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        branches_data = self.request.data.get("branches", [])
        serializer.validate_branches(self.request.data.get("branches", []))
        serializer.save(branches=branches_data)


class RetrieveUpdateDeleteAccountView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrAccountOwner]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @extend_schema(
        operation_id='account_put', exclude=True,
        summary='Update all fields from user',
        description='Update all fields from user',
    )
    def put(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_update(self, serializer):
        branches_data = self.request.data.get("branches", [])
        serializer.validate_branches(self.request.data.get("branches", []))
        serializer.save(branches=branches_data)
