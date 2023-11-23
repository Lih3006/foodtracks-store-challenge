# from rest_framework.views import APIView, Request, Response, status
from .models import Company
from .serializers import CompanySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateCompanyView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDeleteCompanyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


""" class ListCreateCompanyView(APIView):
    def get(self, req: Request) -> Response:
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        serializer = CompanySerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveUpdateDeleteCompanyView(APIView):
    def get(self, req: Request, company_id: int) -> Response:
        company = get_object_or_404(Company, id=company_id)
        serializer = CompanySerializer(company)
        # serializer = AccountSerializer(users)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, req: Request, company_id: int) -> Response:
        company = get_object_or_404(Company, id=company_id)
        serializer = CompanySerializer(company, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req: Request, company_id: int) -> Response:
        company = get_object_or_404(Company, id=company_id)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 """
