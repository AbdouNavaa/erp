# Generated by Django 4.0.6 on 2023-02-05 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0012_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='Taxes',
            field=models.FloatField(default=0.1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='Taxesfourn',
            field=models.FloatField(default=0.1),
            preserve_default=False,
        ),
    ]