# Generated by Django 4.1.5 on 2023-01-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0004_rename_firstname_client_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Factures',
            new_name='Facture',
        ),
    ]