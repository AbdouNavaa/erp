# Generated by Django 4.0.6 on 2023-01-31 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0009_paiements_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiements',
            name='montant',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
