# Generated by Django 3.0 on 2021-05-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leave_management", "0006_auto_20210528_1818"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leave",
            name="in_days",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
