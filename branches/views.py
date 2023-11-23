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

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class RetrieveUpdateDeleteBranchView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsLinkedToBranch]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
