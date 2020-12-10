from django.contrib import admin
from .models import Question, Category

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_title", "created_time", "updated_time"]
    # list_editable = []
    prepopulated_fields = {"slug": ("question_title",)}
    search_fields = ["question_title", "created_time"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["parent", "category_name", "created_time", "updated_time"]
    prepopulated_fields = {"slug": ("category_name",)}
    search_fields = ["category_name", "created_time", "updated_time"]

#
# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ["user", "question", "created_time", "updated_time"]
#     search_fields = ["user", "question", "created_time", "updated_time"]
#
#
# @admin.register(Report)
# class ReportAdmin(admin.ModelAdmin):
#     list_display = [
#         "user",
#         "reported_question",
#         "report_choice",
#         "report_date",
#     ]
#     search_fields = ["reported_question", "report_date"]
