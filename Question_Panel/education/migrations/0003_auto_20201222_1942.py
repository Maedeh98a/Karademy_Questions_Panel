# Generated by Django 3.1 on 2020-12-22 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20201215_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['date_updated'], 'verbose_name': 'یادداشت', 'verbose_name_plural': 'یادداشت ها'},
        ),
    ]
