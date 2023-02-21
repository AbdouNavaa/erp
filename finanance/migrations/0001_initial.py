# Generated by Django 4.0 on 2023-02-19 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('prix', models.FloatField()),
                ('Taxes', models.FloatField()),
                ('Taxesfourn', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PieceCompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.FloatField()),
                ('date_comptable', models.DateField()),
                ('deb', models.FloatField()),
                ('cred', models.FloatField()),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.journal')),
                ('partenaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.client')),
            ],
        ),
        migrations.CreateModel(
            name='Paiements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('montant', models.FloatField()),
                ('Mode', models.CharField(max_length=100)),
                ('Type', models.CharField(choices=[('E', 'Envoyer'), ('R', 'Recevoire')], max_length=1)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.client')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.journal')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_facturation', models.DateField()),
                ('quantity', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.client')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.journal')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.type')),
            ],
        ),
        migrations.CreateModel(
            name='FactureFr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_facturation', models.DateField()),
                ('quantity', models.FloatField()),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.fournisseur')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.journal')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.produit')),
            ],
        ),
        migrations.CreateModel(
            name='FactureCl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_facturation', models.DateField()),
                ('quantity', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.client')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.journal')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.produit')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanance.type'),
        ),
    ]
