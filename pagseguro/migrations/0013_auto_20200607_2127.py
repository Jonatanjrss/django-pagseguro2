# Generated by Django 3.0.7 on 2020-06-07 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagseguro', '0012_remove_authorization_code2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorization',
            old_name='code1',
            new_name='code',
        ),
    ]