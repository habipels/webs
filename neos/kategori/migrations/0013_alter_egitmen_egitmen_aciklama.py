# Generated by Django 3.2.5 on 2021-08-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kategori', '0012_egitmen_egitmen_aciklama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egitmen',
            name='egitmen_aciklama',
            field=models.TextField(max_length=255, null='True'),
        ),
    ]
