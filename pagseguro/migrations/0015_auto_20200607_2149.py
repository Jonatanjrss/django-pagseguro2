# Generated by Django 3.0.7 on 2020-06-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagseguro', '0014_auto_20200607_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, help_text='Código gerado para redirecionamento.', max_length=100, verbose_name='código da requisição')),
                ('date', models.DateTimeField(help_text='Data da solicitação.', verbose_name='Data')),
                ('success', models.BooleanField(db_index=True, default=False, help_text='A solicitação de autorização foi feita com sucesso?', verbose_name='Sucesso')),
                ('message', models.TextField(blank=True, help_text='Mensagem apresentada no caso de erro na solicitação.', verbose_name='Mensagem de erro')),
                ('reference', models.CharField(blank=True, help_text='Código único para controle', max_length=100, unique=True, verbose_name='referencia')),
                ('authorizer_email', models.EmailField(help_text='Email de quem autorizou', max_length=254, verbose_name='Email do autorizador')),
                ('public_key', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Autorização',
                'verbose_name_plural': 'Autorizações',
                'ordering': ['-date'],
            },
        ),
        migrations.AlterModelOptions(
            name='requestauthorization',
            options={'ordering': ['-date'], 'verbose_name': 'Solicitação de Autorização', 'verbose_name_plural': 'Solicitações de Autorização'},
        ),
    ]
