# Generated by Django 3.1 on 2020-12-20 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0008_auto_20201219_2211"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="status",
        ),
        migrations.RemoveField(
            model_name="questionreport",
            name="report_count",
        ),
        migrations.RemoveField(
            model_name="questionreport",
            name="reported_answer",
        ),
    ]
