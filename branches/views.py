# from rest_framework.views import APIView, Request, Response, status
from .models import Branch
from .serializers import BranchSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsStateManager, IsCityManager, IsSiteManager

# from django.shortcuts import get_object_or_404


class ListCreateBranchView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class RetrieveUpdateDeleteBranchView(RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


""" class ListCreateBranchView(APIView):
    def get(self, req: Request) -> Response:
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        serializer = BranchSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveUpdateDeleteBranchView(APIView):
    def get(self, req: Request, branch_id: int) -> Response:
        branch = get_object_or_404(Branch, id=branch_id)
        serializer = BranchSerializer(branch)
        # serializer = AccountSerializer(users)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, req: Request, branch_id: int) -> Response:
        branch = get_object_or_404(Branch, id=branch_id)
        serializer = BranchSerializer(branch, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req: Request, branch_id: int) -> Response:
        branch = get_object_or_404(Branch, id=branch_id)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 """
