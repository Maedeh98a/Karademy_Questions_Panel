from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

STATUS_CHOICE = (
    ('published', 'انتشاریافته'),
    ('draft', 'پیش نویس'))

REPORT_CHOICES = (
    ('inappropiate', 'نامناسب'),
    ('', 'بی ربط'),
    ('', 'حاوی الفاظ سیاسی'),
    ('', 'تبلیغ'),
    ('other', ''),

)


class Category(models.Model):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="دسته بندی ها",
        blank=True,
        default=None,
        null=True,
    )
    category_name = models.CharField(
        max_length=100, null=True, verbose_name="نام دسته بندی"
    )
    created_time = models.DateTimeField(
        auto_now_add=True, null=True, db_index=True, verbose_name=" تاریخ ایجاد"
    )
    updated_time = models.DateTimeField(
        auto_now_add=True, null=True, db_index=True, verbose_name="تاریخ به روز رسانی"
    )
    slug = models.SlugField(null=True)

    class Meta:
        db_table = "Category"
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندیها"

    def __str__(self):
        return self.category_name


class Question(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="سوال کننده"
    )
    question_title = models.CharField(
        max_length=200, null=True, blank=False, verbose_name="عنوان سوال"
    )
    slug = models.SlugField(null=True)
    question_text = models.TextField(blank=False, null=True, verbose_name="متن سوال")
    question_category = models.ManyToManyField(Category, verbose_name="دسته بندی سوال")
    created_time = models.DateTimeField(
        auto_now_add=True, null=True, db_index=True, verbose_name=" تاریخ ایجاد"
    )
    updated_time = models.DateTimeField(
        auto_now_add=True, null=True, db_index=True, verbose_name="تاریخ به روز رسانی"
    )
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default='published', null=True, verbose_name='وضعیت انتشار')
    question_photo = models.ImageField(
        upload_to="question/%Y/%m/%d", blank=True, null=True, verbose_name="تصویر سوال"
    )

    class Meta:
        db_table = "Questions"
        verbose_name = "سوال"
        verbose_name_plural = "سوال ها"

    def __str__(self):
        return self.question_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question_title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("questions:detail_question", kwargs={'slug': self.slug})

# class Tags(models.Model):
#     tag_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='برچسب')


class Answer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, verbose_name="پاسخ دهنده"
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="سوال"
    )
    answer = models.TextField(null=True, blank=False, verbose_name="پاسخ")
    created_time = models.DateTimeField(auto_now=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default='published', null=True,
        verbose_name='وضعیت انتشار')

    class Meta:
        db_table = "Answers"
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ ها"

    def __str__(self):
        return self.question.question_title


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='گزارش دهنده')
    reported_question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE, verbose_name='سوال گزارش شده')
    # I got problem here ...
    reported_answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE, verbose_name='پاسخ گزارش شده')
    report_choice = models.CharField(max_length=30, choices=REPORT_CHOICES, blank=False, null=True, verbose_name='گزینه های گزارش')
    report_description = models.TextField(blank=True, null=True, verbose_name='متن گزارش')
    report_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ گزارش')
    report_count = models.IntegerField(verbose_name='تعداد گزارش')