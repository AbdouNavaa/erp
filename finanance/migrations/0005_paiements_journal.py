# Generated by Django 4.0.6 on 2023-02-08 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0004_remove_paiements_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiements',
            name='journal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='finanance.journal'),
            preserve_default=False,
        ),
    ]
