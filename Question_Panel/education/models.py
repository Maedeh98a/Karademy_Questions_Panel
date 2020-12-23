from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

NOTE_STATUS = (
    ("draft", "پیش نویس"),
    ("publish", "انتشار"),
)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    note_title = models.CharField(max_length=40, blank=False, verbose_name="عنوان")
    slug = models.SlugField(allow_unicode=True, null=True, verbose_name="")
    note_body = RichTextField(blank=False, verbose_name="متن")
    note_status = models.CharField(
        max_length=8, choices=NOTE_STATUS, null=True, verbose_name="وضعیت "
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="تاریخ به روز رسانی"
    )

    def __str__(self):
        return f"{self.user.username}ایجاد شده توسط {self.note_title}متن با عنوان"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.note_title, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_created']
        db_table = "note"
        verbose_name = "یادداشت"
        verbose_name_plural = "یادداشت ها"

    def get_absolute_url(self):
        return reverse("education:update_note", kwargs={'slug': self.slug})



class Comment(models.Model):
    pass
