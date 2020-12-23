# Generated by Django 3.1 on 2020-12-19 18:41

from django.conf import settings
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("questions", "0007_auto_20201215_1141"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="question_like",
            field=models.ManyToManyField(
                blank=True, related_name="questions_like", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="tag",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
