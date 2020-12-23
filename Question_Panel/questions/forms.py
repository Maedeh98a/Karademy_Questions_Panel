from django.forms import ModelForm
from .models import Category, Question, Answer, AnswerReport, QuestionReport, Tag


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["tag_name"]


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            "question_title",
            "question_text",
            "question_category",
            "question_tag",
        ]


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["answer_body"]


class QuestionReportForm(ModelForm):
    class Meta:
        model = QuestionReport
        fields = ["report_choice", "report_description"]


class AnswerReportForm(ModelForm):
    class Meta:
        model = AnswerReport
        fields = ["report_choice", "report_description"]
