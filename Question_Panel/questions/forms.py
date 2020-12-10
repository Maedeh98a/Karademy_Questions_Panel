from django.forms import ModelForm
from .models import Question, Answer, AnswerReport, QuestionReport


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["question_title", "question_text", "question_category"]


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["answer"]


class QuestionReportForm(ModelForm):
    class Meta:
        model = QuestionReport
        fields = ["report_choice", "report_description"]


class AnswerReportForm(ModelForm):
    class Meta:
        model = AnswerReport
        fields = ["report_choice", "report_description"]