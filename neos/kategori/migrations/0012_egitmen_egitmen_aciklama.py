# Generated by Django 3.2.5 on 2021-08-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kategori', '0011_auto_20210820_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='egitmen',
            name='egitmen_aciklama',
            field=models.CharField(max_length=255, null='True'),
            preserve_default='True',
        ),
    ]
