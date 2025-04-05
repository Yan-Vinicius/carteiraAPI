from decimal import Decimal, InvalidOperation
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Carteira, Transacao
from .serializers import UserSerializer, CarteiraSerializer, TransacaoSerializer
from django.utils.dateparse import parse_date


class CriarUsuarioView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CarteiraView(APIView):
    # Autenticação do usuário e suas permissões
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        carteira = Carteira.objects.get(user=request.user)
        serializer = CarteiraSerializer(carteira)
        return Response(serializer.data)


class DepositarView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        quantidade = Decimal(str(request.data.get('quantidade')))
        carteira = Carteira.objects.get(user=request.user)
        carteira.saldo += quantidade
        carteira.save()
        return Response({'messagem': 'Depósito feito com sucesso', 'novo_saldo': carteira.saldo})


class TransferenciaView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        receiver_id = request.data.get('receiver_id')

        try:
            amount = Decimal(str(request.data.get('amount')))
            if amount <= 0:
                return Response({'error': 'Valor inválido'}, status=400)
        except (InvalidOperation, TypeError):
            return Response({'error': 'Valor da transferência inválido'}, status=400)

        pagador_wallet = Carteira.objects.get(user=request.user)
        destinatario_wallet = Carteira.objects.get(user_id=receiver_id)

        if pagador_wallet.saldo < amount:
            return Response({'error': 'Saldo insuficiente'}, status=400)

        pagador_wallet.saldo -= amount
        destinatario_wallet.saldo += amount
        pagador_wallet.save()
        destinatario_wallet.save()

        Transacao.objects.create(pagador=request.user, destinatario_id=receiver_id, valor_transacao=amount)
        return Response({'messagem': 'transferência feita com sucesso'})


class ListarTransacaoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data_inicio = request.GET.get('start')
        data_fim = request.GET.get('end')

        transactions = Transacao.objects.filter(pagador=request.user)

        if data_inicio and data_fim:
            transactions = transactions.filter(data_transacao__range=[parse_date(data_inicio), parse_date(data_fim)])

        serializer = TransacaoSerializer(transactions, many=True)
        print("Usuário:", request.user)
        print("Transações encontradas:", transactions.count())
        return Response(serializer.data)

