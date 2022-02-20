from django.contrib import admin
from .models import Purse, Wallet, Photo

# Register your models here.
admin.site.register(Purse)
admin.site.register(Wallet)
admin.site.register(Photo)