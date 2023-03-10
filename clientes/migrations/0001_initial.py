# Generated by Django 4.1.2 on 2022-11-06 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("sobrenome", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("cpf", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="Computador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("computador", models.CharField(max_length=40)),
                ("tipo", models.CharField(max_length=40)),
                ("modelo", models.CharField(max_length=40)),
                ("descricao", models.CharField(max_length=100)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clientes.cliente",
                    ),
                ),
            ],
        ),
    ]
