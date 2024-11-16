from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from tutorial.quickstart.serializers import UserSerializer

from users.models import Payment, User
from users.serializers import PaymentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("course", "lesson", "payment_method")
    ordering_fields = ('payment_date',)
    ordering = ('-payment_date',)