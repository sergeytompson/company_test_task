# Generated by Django 4.2 on 2023-04-07 12:53

import company_api.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="worker",
            name="first_name",
            field=models.CharField(default="Имя", max_length=150, verbose_name="Имя"),
        ),
        migrations.AddField(
            model_name="worker",
            name="last_name",
            field=models.CharField(
                default="Фамилия", max_length=150, verbose_name="Фамилия"
            ),
        ),
        migrations.AddField(
            model_name="worker",
            name="patronymic",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="Отчество"
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="age",
            field=models.PositiveIntegerField(
                validators=[company_api.validators.validate_not_too_old],
                verbose_name="Возраст",
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="salary",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[company_api.validators.validate_positive_float],
                verbose_name="Оклад",
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="name",
            field=models.CharField(
                verbose_name="ФИО",
                max_length=150,
                default="Фамилия Имя Отчество",
            ),
        ),
    ]
