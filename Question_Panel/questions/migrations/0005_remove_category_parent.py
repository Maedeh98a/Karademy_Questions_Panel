# Generated by Django 3.1 on 2020-12-12 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0004_auto_20201213_0138"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="parent",
        ),
    ]
