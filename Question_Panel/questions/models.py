from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

STATUS_CHOICE = (("published", "انتشاریافته"), ("draft", "پیش نویس"))

REPORT_CHOICES = (
    ("inappropriate", "نامناسب"),
    ("irrelevant", "بی ربط"),
    ("Contains political words", "حاوی الفاظ سیاسی"),
    ("Contains ads", "تبلیغ"),
    ("other", "دیگر"),
)


class Category(models.Model):

    category_name = models.CharField(
        max_length=100, null=True, verbose_name="نام دسته بندی"
    )
    created_time = models.DateTimeField(
        auto_now_add=True, null=True, db_index=True, verbose_name=" تاریخ ایجاد"
    )
    updated_time = models.DateTimeField(
        auto_now_add=True, null=True, db_index=True, verbose_name="تاریخ به روز رسانی"
    )
    slug = models.SlugField(null=True, allow_unicode=True)

    class Meta:
        db_table = "Category"
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندیها"

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("questions:category", kwargs={"slug": self.slug})


class Tag(models.Model):
    tag_name = models.CharField(max_length=12, blank=True, verbose_name="برچسب ها")
    # check again : slug = models.SlugField(null=True, allow_unicode=True)
    created_time = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="تاریخ ایجاد"
    )
    updated_time = models.DateTimeField(
        auto_now=True, null=True, verbose_name="تاریخ به روزرسانی"
    )

    class Meta:
        db_table = "tags"
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"

    def __str__(self):
        return self.tag_name


class Question(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="سوال کننده"
    )
    question_title = models.CharField(
        max_length=200, null=True, blank=False, verbose_name="عنوان سوال"
    )
    slug = models.SlugField(null=True, allow_unicode=True)
    question_text = RichTextField(blank=False, null=True, verbose_name="متن سوال")
    question_category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="دسته بندی سوال",
        related_name="questions",
    )
    question_tag = models.ManyToManyField(Tag, blank=True, verbose_name="برچسب")
    tag = TaggableManager()
    created_time = models.DateTimeField(
        auto_now_add=True, null=True, db_index=True, verbose_name=" تاریخ ایجاد"
    )
    updated_time = models.DateTimeField(
        auto_now=True, null=True, db_index=True, verbose_name="تاریخ به روز رسانی"
    )
    answered = models.BooleanField(null=True, blank=True, verbose_name="پاسخ داده شده ")
    question_like = models.ManyToManyField(
        User, related_name="questions_like", blank=True
    )
    total = models.IntegerField

    class Meta:
        db_table = "Questions"
        verbose_name = "سوال"
        verbose_name_plural = "سوال ها"
        ordering = ["-updated_time"]

    def number_of_likes(self):
        return self.question_like.count()

    def __str__(self):
        return str(self.question_title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question_title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("questions:question_detail", kwargs={"slug": self.slug})


class Answer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="پاسخ دهنده"
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="سوال", related_name="answers"
    )
    answer_body = RichTextField(null=True, blank=False, verbose_name="پاسخ")
    created_time = models.DateTimeField(auto_now=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICE,
        default="draft",
        null=True,
        verbose_name="وضعیت انتشار",
    )
    answer_like = models.ManyToManyField(User, related_name="answers_like", blank=True)

    class Meta:
        db_table = "Answers"
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ ها"

    def __str__(self):
        return str(self.question.question_title)

    def number_of_likes(self):
        return self.answer_like.count()


class QuestionReport(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="گزارش دهنده"
    )
    reported_question = models.ForeignKey(
        Question,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="سوال گزارش شده",
    )
    report_choice = models.CharField(
        max_length=30,
        choices=REPORT_CHOICES,
        blank=False,
        null=True,
        verbose_name="گزینه های گزارش",
    )
    report_description = RichTextField(blank=True, null=True, verbose_name="متن گزارش")
    report_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ گزارش")

    class Meta:
        verbose_name = "گزارش سوال "
        verbose_name_plural = "گزارش سوال ها"

    def number_of_reports(self):
        return self.reported_question.count()


class AnswerReport(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="گزارش دهنده"
    )
    reported_answer = models.ForeignKey(
        Answer,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="پاسخ گزارش شده",
    )
    report_choice = models.CharField(
        max_length=30,
        choices=REPORT_CHOICES,
        blank=False,
        null=True,
        verbose_name="گزینه های گزارش",
    )
    report_description = RichTextField(blank=True, null=True, verbose_name="متن گزارش")
    report_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ گزارش")
    report_count = models.IntegerField(
        verbose_name="تعداد گزارش", null=True, blank=True
    )

    class Meta:
        verbose_name = "گزارش پاسخ"
        verbose_name_plural = "گزارش های پاسخ ها"
