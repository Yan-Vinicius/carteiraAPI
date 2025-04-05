from django.contrib.auth.models import User
from Models.models import Carteira
import random

# Criação de usuários fictícios para popular o banco de dados
usuarios = []
for i in range(10):
    user = User.objects.create_user(username=f'user{i}', password='123456')
    Carteira.objects.create(user=user, balance=random.uniform(50, 500))
    usuarios.append(user)
