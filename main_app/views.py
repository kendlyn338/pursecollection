from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Purse, Wallet, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'pursecollection'

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
    wallets_purse_doesnt_have = Wallet.objects.exclude(
        id__in = purse.wallets.all().values_list('id'))
    return render(request, 'purses/detail.html', {
        'purse': purse,
        'wallets': wallets_purse_doesnt_have
    })


class PurseCreate(CreateView):
    model = Purse
    fields = ('brand', 'style', 'color', 'price')


class PurseUpdate(UpdateView):
    model = Purse
    fields = ('brand', 'style', 'color', 'price')


class PurseDelete(DeleteView):
    model = Purse
    success_url = '/purses/'


def wallets_index(request):
    wallets = Wallet.objects.all()
    return render(request, 'wallets/index.html', {'wallets': wallets})

def wallets_detail(request, wallet_id):
    wallet = Wallet.objects.get(id=wallet_id)
    return render(request, 'wallets/detail.html', {'wallet': wallet})

def assoc_wallet(request, purse_id, wallet_id):
    Purse.objects.get(id=purse_id).wallets.add(wallet_id)
    return redirect('purses_detail', purse_id=purse_id)


def add_photo(request, purse_id):
    photo_file = request.FILES.get('photo-file')
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
             photo_file.name[photo_file.name.rfind('.')]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, purse_id=purse_id)
            photo.save()
        except Exception as error:
            print('*****************')
            print('An error has occurred with s3:')
            print(error)
            print('*****************')
    return redirect('purses_detail', purse_id=purse_id)


class WalletCreate(CreateView):
    model = Wallet
    fields = '__all__'


class WalletUpdate(UpdateView):
    model = Wallet
    fields = '__all__'


class WalletDelete(DeleteView):
    model = Wallet
    success_url = '/wallets/'

