# Generated by Django 3.1 on 2020-12-22 16:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='درباره من '),
        ),
    ]