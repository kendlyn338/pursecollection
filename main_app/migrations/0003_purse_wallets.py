# Generated by Django 4.0.2 on 2022-02-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='purse',
            name='wallets',
            field=models.ManyToManyField(to='main_app.Wallet'),
        ),
    ]