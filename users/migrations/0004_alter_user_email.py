# Generated by Django 4.2.2 on 2024-09-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_payment_id_delete_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Email"
            ),
        ),
    ]
