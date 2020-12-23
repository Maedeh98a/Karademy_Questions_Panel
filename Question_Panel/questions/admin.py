from django.contrib import admin
from jalali_date.admin import (
    ModelAdminJalaliMixin,
    StackedInlineJalaliMixin,
    TabularInlineJalaliMixin,
)
from jalali_date import datetime2jalali
from .models import Question, Category, Answer, QuestionReport, AnswerReport, Tag


@admin.register(Question)
class QuestionAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # def question_report(self, obj):
    #     total = QuestionReport.objects.count()
    #     amount = Question.total
    #     return amount

    list_display = [
        "question_title",
        "j_created",
        "j_updated",
        "question_category",
        "tag_to_str",
    ]
    # list_editable = []
    prepopulated_fields = {"slug": ("question_title",)}
    search_fields = ["question_title", "j_created", "question_category", "tag_to_str"]

    def j_created(self, obj):
        return datetime2jalali(obj.created_time).strftime("%y/%m/%d _ %H:%M:%S")

    def j_updated(self, obj):
        return datetime2jalali(obj.updated_time).strftime("%y/%m/%d _ %H:%M:%S")

    j_created.short_description = "تاریخ ایجاد "
    j_updated.short_description = "تاریخ به روز رسانی"

    def tag_to_str(self, obj):
        return "،".join([tag.tag_name for tag in obj.question_tag.all()])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name", "created_time", "updated_time"]
    prepopulated_fields = {"slug": ("category_name",)}
    search_fields = ["category_name", "created_time", "updated_time"]

    def j_created(self, obj):
        return datetime2jalali(obj.created_time).strftime("%y/%m/%d _ %H:%M:%S")

    def j_updated(self, obj):
        return datetime2jalali(obj.updated_time).strftime("%y/%m/%d _ %H:%M:%S")

    j_created.short_description = "تاریخ ایجاد "
    j_updated.short_description = "تاریخ به روز رسانی"


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["tag_name", "created_time", "updated_time"]
    # prepopulated_fields = {"slug": ("tag_name",)}
    search_fields = ["tag_name", "created_time", "updated_time"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["user", "j_created", "j_updated"]
    search_fields = ["user", "j_created", "j_updated"]

    def j_created(self, obj):
        return datetime2jalali(obj.created_time).strftime("%y/%m/%d _ %H:%M:%S")

    def j_updated(self, obj):
        return datetime2jalali(obj.updated_time).strftime("%y/%m/%d _ %H:%M:%S")

    j_created.short_description = "تاریخ ایجاد "
    j_updated.short_description = "تاریخ به روز رسانی"


@admin.register(QuestionReport)
class QuestionReportAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "reported_question",
        "report_choice",
        "j_created",
    ]
    search_fields = ["reported_question", "j_created"]

    def j_created(self, obj):
        return datetime2jalali(obj.report_date).strftime("%y/%m/%d _ %H:%M:%S")

    j_created.short_description = "تاریخ ایجاد "


@admin.register(AnswerReport)
class QuestionReportAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "reported_answer",
        "report_choice",
        "j_created",
    ]
    search_fields = ["reported_answer", "j_created"]

    def j_created(self, obj):
        return datetime2jalali(obj.report_date).strftime("%y/%m/%d _ %H:%M:%S")

    j_created.short_description = "تاریخ ایجاد "
