# from rest_framework.views import APIView, Request, Response, status
from .models import Account
from .serializers import AccountSerializer  #
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from django.shortcuts import get_object_or_404


""" class ListCreateAccountView(APIView):
    def get(self, req: Request) -> Response:
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        # serializer = AccountSerializer(users)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        serializer = AccountSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class RetrieveUpdateDeleteAccountView(APIView):
    def get(self, req: Request, account_id: int) -> Response:
        account = get_object_or_404(Account, id=account_id)
        serializer = AccountSerializer(account)
        # serializer = AccountSerializer(users)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, req: Request, account_id: int) -> Response:
        account = get_object_or_404(Account, id=account_id)
        serializer = AccountSerializer(account, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req: Request, account_id: int) -> Response:
        account = get_object_or_404(Account, id=account_id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 """


class ListCreateAccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        serializer.save()


class RetrieveUpdateDeleteAccountView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
