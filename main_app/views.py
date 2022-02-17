from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Purse, Wallet

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def purses_index(request):
    purses = Purse.objects.all()
    return render(request, 'purses/index.html', {'purses': purses})


def purses_detail(request, purse_id):
    purse = Purse.objects.get(id=purse_id)
    return render(request, 'purses/detail.html', {'purse': purse})


class PurseCreate(CreateView):
    model = Purse
    fields = '__all__'


class PurseUpdate(UpdateView):
    model = Purse
    fields = '__all__'


class PurseDelete(DeleteView):
    model = Purse
    success_url = '/purses/'


def wallets_index(request):
    wallets = Wallet.objects.all()
    return render(request, 'wallets/index.html', {'wallets': wallets})

def wallets_detail(request, wallet_id):
    wallet = Wallet.objects.get(id=wallet_id)
    return render(request, 'wallets/detail.html', {'wallet': wallet})

class WalletCreate(CreateView):
    model = Wallet
    fields = '__all__'


class WalletUpdate(UpdateView):
    model = Wallet
    fields = '__all__'


class WalletDelete(DeleteView):
    model = Wallet
    success_url = '/wallets/'

