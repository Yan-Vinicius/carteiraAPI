from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CriarUsuarioView, CarteiraView, DepositarView, TransferenciaView, ListarTransacaoView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', CriarUsuarioView.as_view(), name='create_user'),
    path('users/wallet/', CarteiraView.as_view(), name='wallet'),

    path('wallet/deposit/', DepositarView.as_view(), name='deposit'),
    path('wallet/transfer/', TransferenciaView.as_view(), name='transfer'),
    path('wallet/transactions/', ListarTransacaoView.as_view(), name='transactions'),
]