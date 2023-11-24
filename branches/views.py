from .models import Branch
from .serializers import BranchSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsLinkedToBranch


class ListCreateBranchView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsLinkedToBranch]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get_queryset(self):
        company_parameter = self.request.query_params.get("company_id")
        role_parameter = self.request.query_params.get("role")
        if company_parameter:
            queryset = Branch.objects.filter(company_id=company_parameter)
            return queryset
        if role_parameter:
            queryset = Branch.objects.filter(accounts__role=role_parameter)
            return queryset

        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class RetrieveUpdateDeleteBranchView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsLinkedToBranch]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
