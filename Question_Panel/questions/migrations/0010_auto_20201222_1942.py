# Generated by Django 3.1 on 2020-12-22 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0009_auto_20201220_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-updated_time'], 'verbose_name': 'سوال', 'verbose_name_plural': 'سوال ها'},
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_like',
            field=models.ManyToManyField(blank=True, related_name='answers_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questions.category', verbose_name='دسته بندی سوال'),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='تاریخ به روز رسانی'),
        ),
    ]
