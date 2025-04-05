from django.contrib.auth.models import User
from django.db import models


# model da carteira
# A criação do usuário já é feita usando o primeiro import deste arquivo
class Carteira(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    def __str__(self):
        return f"Carteira de {self.user.username}"


# model da transação
class Transacao(models.Model):

    pagador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transacao_enviada')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transacao_recebida')
    valor_transacao = models.DecimalField(max_digits=10, decimal_places=2)
    data_transacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pagador.username} → {self.destinatario.username} | R$ {self.valor_transacao}"

