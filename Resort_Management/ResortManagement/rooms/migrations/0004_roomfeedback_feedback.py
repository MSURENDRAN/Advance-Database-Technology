# Generated by Django 4.2 on 2023-05-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0003_roomfeedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="roomfeedback",
            name="feedback",
            field=models.TextField(default="", max_length=400),
        ),
    ]
