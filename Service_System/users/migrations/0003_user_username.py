# Generated by Django 5.0 on 2023-12-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_is_staff"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.TextField(default="tester1", max_length=100),
            preserve_default=False,
        ),
    ]
