from .models import Branch
from .serializers import BranchSerializer
from companies.models import Company
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsLinkedToBranch
from rest_framework.serializers import ValidationError


class ListCreateBranchView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsLinkedToBranch]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get_queryset(self):
        user = self.request.user

        # Se o usuário é um superusuário, mostra todas as branches da sua company
        if user.is_superuser:
            return Branch.objects.filter(company=user.company)

        # Se o usuário é vinculado a pelo menos uma branch, mostra essas branches
        elif user.branches.exists():
            return user.branches.all()

        # Se o usuário é vinculado a uma empresa, mostra as branches da empresa
        elif user.company:
            return Branch.objects.filter(company=user.company)

    """ def get_queryset(self):
        company_parameter = self.request.query_params.get("company_id")
        role_parameter = self.request.query_params.get("role")
        if company_parameter:
            queryset = Branch.objects.filter(company_id=company_parameter)
            return queryset
        if role_parameter:
            queryset = Branch.objects.filter(accounts__role=role_parameter)
            return queryset

        return super().get_queryset() """

    def perform_create(self, serializer):
        try:
            print("teste", self.request.user.company)
            serializer.save(company=self.request.user.company)

        except Company.DoesNotExist:
            raise ValidationError({"message": "You need a company to create a branch."})


class RetrieveUpdateDeleteBranchView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsLinkedToBranch]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
