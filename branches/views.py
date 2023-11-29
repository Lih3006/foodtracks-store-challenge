from .models import Branch
from .serializers import BranchSerializer
from companies.models import Company
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsLinkedToBranch
from rest_framework.serializers import ValidationError
from drf_spectacular.utils import extend_schema


class ListCreateBranchView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsLinkedToBranch]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get_queryset(self):
        user = self.request.user
        state_parameter = self.request.query_params.get("state")
        city_parameter = self.request.query_params.get("city")

        if state_parameter:
            return Branch.objects.filter(state__icontains=state_parameter)

        if city_parameter:
            return Branch.objects.filter(city__icontains=city_parameter)

        if not hasattr(user, 'company') and not user.branches.all():
            return Branch.objects.none()
        elif user.is_superuser:
            return Branch.objects.filter(company=user.company)
        elif user.branches.exists():
            return user.branches.all()
        elif user.company:
            return Branch.objects.filter(company=user.company)

    def perform_create(self, serializer):
        try:
            serializer.save(company=self.request.user.company)
        except Company.DoesNotExist:
            raise ValidationError({"message": "You need a company to create a branch."})


class RetrieveUpdateDeleteBranchView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLinkedToBranch]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    @extend_schema(
        operation_id='branch_put', exclude=True,
        summary='Update all fields from Branch',
        description='Update all fields from Branch',
    )
    def put(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)