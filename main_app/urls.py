from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('purses/', views.purses_index, name='purses_index'),
    path('purses/<int:purse_id>/', views.purses_detail, name='purses_detail'),
    path('purses/create/', views.PurseCreate.as_view(), name='purses_create'),
    path('purses/<int:pk>/update/', views.PurseUpdate.as_view(), name='purses_update'),
    path('purses/<int:pk>/delete/', views.PurseDelete.as_view(), name='purses_delete'),
    
    path('wallets/', views.wallets_index, name='wallets_index'),
    path('wallets/<int:wallet_id>/', views.wallets_detail, name='wallets_detail'),
    path('wallets/create/', views.WalletCreate.as_view(), name='wallets_create'),
    path('wallets/<int:pk>/update/', views.WalletUpdate.as_view(), name='wallets_update'),
    path('wallets/<int:pk>/delete/', views.WalletDelete.as_view(), name='wallets_delete'),
    path('purses/<int:purse_id>/assoc_wallet/<int:wallet_id>/', views.assoc_wallet, name='assoc_wallet'),
    path('purses/<int:purse_id>/add_photo/', views.add_photo, name='add_photo'),
]