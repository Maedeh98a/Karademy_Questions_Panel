from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import (
    QuestionForm,
    QuestionReportForm,
    AnswerReportForm,
    AnswerForm,
    TagForm,
)
from .models import Question, Answer, AnswerReport, QuestionReport, Category
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST


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


def category(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    context = {"categories": categories}
    return render(request, "questions/categories.html", context)


@login_required()
def create_question(request):
    tag_form = TagForm()
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        tag_form = TagForm(request.POST)
        if form.is_valid() and tag_form.is_valid():
            new_question = form.save()
            new_tag = tag_form.save()
            # new_question.question_tag.set = new_tag ===> it's many to many
            new_question.user = request.user
            new_question.save()
            return redirect("/")

    context = {"form": form, "tag_form": tag_form}
    return render(request, "questions/ask_question.html", context)


def like(request):
    pass
    # user = request.user
    # if request.method == 'post':
    #     question_id = request.POST.get('question_id')
    #     question_obj = Question.objects.get(id=question_id)
    #
    #     if user in question_obj.question_like.all():
    #         question_obj.question_like.remove(user)
    #     else:
    #         question_obj.question_like.add(user)
    #
    #         # like table ==> arian
    # return redirect("questions:question_list")


@login_required()
@require_POST
def question_like(request, pk):
    question = get_object_or_404(Question, id=request.POST.get("question_id"))
    if question.question_like.filter(id=request.user.id).exists():
        question.question_like.remove(request.user)
    else:
        question.question_like.add(request.user)
    return HttpResponseRedirect(reverse("questions:question_detail", args=[str(pk)]))


@login_required()
def create_answer(request, pk):
    question = get_object_or_404(Question, id=pk)
    new_answer = None
    form = AnswerForm()
    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.question = Question.objects.get(id=pk)
            new_answer.user = request.user
            new_answer.save()
            return redirect("/")
    else:
        form = AnswerForm
    return render(
        request,
        "questions/create_answer.html",
        {
            "questions": question,
            "new_answer": new_answer,
            "form": form,
        },
    )


# def detail(request, pk):
#     question = get_object_or_404(Question, id=pk)
#     answers = question.answers.all()
#     context = {"answers": answers}
#     return render(request, "questions/question_detail.html", context)
class QuestionDetailView(DetailView):
    model = Question
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Question, id=self.kwargs["pk"])

        liked = False
        if likes_connected.question_like.filter(id=self.request.user.id).exists():
            liked = True
        data["number_of_likes"] = likes_connected.number_of_likes()
        data["post_is_liked"] = liked
        return data


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


@login_required()
def update_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    form = AnswerForm(instance=answer)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "questions/create_answer.html", context)


@login_required()
def delete_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    if request.method == "POST":
        answer.delete()
        return redirect("/")
    context = {"item": answer}
    return render(request, "questions/delete_answer.html", context)


@login_required()
def report_question(request, pk):
    question = Question.objects.get(id=pk)
    form = QuestionReportForm()
    if request.method == "POST":
        form = QuestionReportForm(request.POST)
        if form.is_valid():
            new_report = form.save()
            new_report.user = request.user
            new_report.reported_question = Question.objects.get(id=pk)
            new_report.save()
            return redirect("questions:question_list")
    return render(
        request, "questions/question_report.html", {"form": form, "question": question}
    )


@login_required()
def report_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    form = AnswerReportForm()
    if request.method == "POST":
        form = AnswerReportForm(request.POST)
        if form.is_valid():
            new_report = form.save()
            new_report.user = request.user
            new_report.reported_answer = Answer.objects.get(id=pk)
            new_report.save()
            return redirect("questions:question_list")
    return render(
        request, "questions/answer_report.html", {"form": form, "answer": answer}
    )
