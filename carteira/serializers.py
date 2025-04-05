from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Carteira, Transacao


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Carteira.objects.create(user=user)
        return user


class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carteira
        fields = ['saldo']


class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['pagador', 'destinatario', 'valor_transacao', 'data_transacao']
