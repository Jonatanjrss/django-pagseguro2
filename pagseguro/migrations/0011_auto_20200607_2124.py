# Generated by Django 3.0.7 on 2020-06-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagseguro', '0010_auto_20200607_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorization',
            name='code2',
            field=models.CharField(blank=True, help_text='Código gerado para redirecionamento.', max_length=100, verbose_name='código da resposta'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='code1',
            field=models.CharField(blank=True, help_text='Código gerado para redirecionamento.', max_length=100, verbose_name='código da requisição'),
        ),
    ]