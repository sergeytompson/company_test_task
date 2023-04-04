# Generated by Django 4.2 on 2023-04-04 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, verbose_name="Название департамента"
                    ),
                ),
            ],
            options={
                "verbose_name": "Департамент",
                "verbose_name_plural": "Департаменты",
            },
        ),
        migrations.CreateModel(
            name="Worker",
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
                ("name", models.CharField(max_length=150, verbose_name="ФИО")),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="workers/", verbose_name="Фото"
                    ),
                ),
                (
                    "salary",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Оклад"
                    ),
                ),
                ("age", models.PositiveIntegerField(verbose_name="Возраст")),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="company_api.department",
                        verbose_name="Департамент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
            },
        ),
        migrations.AddField(
            model_name="department",
            name="director",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="department_director",
                to="company_api.worker",
                verbose_name="Директор департамента",
            ),
        ),
    ]
