# Generated by Django 4.2.3 on 2023-07-29 01:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Buyer",
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
                ("name", models.CharField(max_length=64)),
                ("email", models.CharField(max_length=64)),
                ("password", models.CharField(max_length=64)),
                ("phoneNo", models.CharField(max_length=64)),
                ("address", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Seller",
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
                ("name", models.CharField(max_length=64)),
                ("email", models.CharField(max_length=64)),
                ("password", models.CharField(max_length=64)),
                ("phoneNo", models.CharField(max_length=64)),
                ("address", models.CharField(max_length=100)),
                ("experience", models.CharField(max_length=100)),
            ],
        ),
    ]
