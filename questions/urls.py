from django.urls import path
from . import views


app_name = "questions"
urlpatterns = [
    path("question_list/", views.QuestionList.as_view(), name="question_list"),
    path("my_question/", views.MyQuestionList.as_view(), name="my_question"),
    path("create_question/", views.create_question, name="create_question"),
    path("update_question/<str:pk>", views.update_question, name="update_question"),
    path("delete_question/<str:pk>", views.delete_question, name="delete_question"),
    path("<str:slug>", views.delete_question, name="detail_question"),

]
