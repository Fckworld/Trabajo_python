# Generated by Django 4.2.1 on 2023-05-20 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mesa",
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
                ("numero", models.IntegerField()),
                ("capacidad", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Reserva",
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
                ("fecha", models.DateField()),
                ("hora", models.TimeField()),
                ("nombre_cliente", models.CharField(max_length=100)),
                ("email_cliente", models.EmailField(max_length=254)),
                ("telefono_cliente", models.CharField(max_length=20)),
                (
                    "mesa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="reservas.mesa"
                    ),
                ),
            ],
        ),
    ]