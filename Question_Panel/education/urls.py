from django.urls import path
from . import views

app_name = "education"
urlpatterns = [
    path("", views.NoteList.as_view(), name="note_list"),
    path("my_note", views.MyNote.as_view(), name="my_note"),

    path("create_note", views.CreateNote.as_view(), name="create_note"),
    path('<pk>/edit/', views.UpdateNote.as_view(), name='update_note'),
]
