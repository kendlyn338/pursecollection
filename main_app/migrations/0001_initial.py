# Generated by Django 4.0.2 on 2022-02-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
