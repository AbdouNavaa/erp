# Generated by Django 4.0.6 on 2023-02-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0010_paiements_montant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturecl',
            old_name='HTaxe',
            new_name='Taxe',
        ),
        migrations.RenameField(
            model_name='facturefr',
            old_name='HTaxe',
            new_name='Taxe',
        ),
        migrations.RemoveField(
            model_name='facturecl',
            name='code',
        ),
        migrations.RemoveField(
            model_name='facturefr',
            name='code',
        ),
        migrations.RemoveField(
            model_name='paiements',
            name='code',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='quantity',
        ),
        migrations.AddField(
            model_name='facturecl',
            name='quantity',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facturefr',
            name='quantity',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]