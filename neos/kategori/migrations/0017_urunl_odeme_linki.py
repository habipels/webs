# Generated by Django 3.2.5 on 2021-08-24 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kategori', '0016_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='urunl',
            name='odeme_linki',
            field=models.CharField(max_length=100, null='True'),
            preserve_default='True',
        ),
    ]
