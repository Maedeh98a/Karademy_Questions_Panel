# Generated by Django 3.1 on 2020-12-13 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0005_remove_category_parent"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="slug",
        ),
    ]