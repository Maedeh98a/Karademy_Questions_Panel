from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
from .models import Question
from django.views.generic import ListView
from django.contrib.auth.models import User


class QuestionList(ListView):
    queryset = Question.objects.all()
    template_name = "questions/list_question.html"
    context_object_name = "questions"


class MyQuestionList(LoginRequiredMixin, ListView):
    model = Question
    template_name = "questions/my_question.html"
    context_object_name = "questions"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user__in=[self.request.user])


@login_required()
def create_question(request):
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save()
            new_question.user = request.user
            new_question.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "questions/ask_question.html", context)


@login_required()
def create_answer(request, **kwargs):
    question = get_object_or_404(Question, **kwargs)
    answers = question.answers.all()
    new_answer = None
    form = AnswerForm()
    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save()
            new_answer.question = question
            new_answer.user = request.user
            new_answer.save()
            return redirect("/")
    else:
        form = AnswerForm
    return render(
        request,
        "questions/question_detail.html",
        {
            "questions": question,
            "answers": answers,
            "new_answer": new_answer,
            "form": form,
        },
    )


@login_required()
def update_question(request, pk):
    question = Question.objects.get(id=pk)
    form = QuestionForm(instance=question)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "questions/ask_question.html", context)


@login_required()
def delete_question(request, pk):
    question = Question.objects.get(id=pk)
    if request.method == "POST":
        question.delete()
        return redirect("/")
    context = {"item": question}
    return render(request, "questions/delete.html", context)
