from django.urls import path
from . import views


app_name = "questions"
urlpatterns = [
    path("question_list/", views.QuestionList.as_view(), name="question_list"),
    path("my_question/", views.MyQuestionList.as_view(), name="my_question"),
    path("create_question/", views.create_question, name="create_question"),
    path("category/<slug>", views.category, name="category"),
    path("blogpost-like1", views.like, name="blogpost_like1"),
    path("blogpost-like/<int:pk>", views.question_like, name="blogpost_like"),
    path("update_question/<str:pk>", views.update_question, name="update_question"),
    path("delete_question/<str:pk>", views.delete_question, name="delete_question"),
    path("update_answer/<str:pk>", views.update_answer, name="update_answer"),
    path("delete_answer/<str:pk>", views.delete_answer, name="delete_answer"),
    path("report_question/<str:pk>", views.report_question, name="report_question"),
    path("report_answer/<str:pk>", views.report_answer, name="report_answer"),
    path("create/<str:pk>", views.create_answer, name="create_answer"),
    path("detail/<str:pk>", views.QuestionDetailView.as_view(), name="question_detail"),
    # path("detail/<str:pk>", views.detail, name="question_detail"),
]
