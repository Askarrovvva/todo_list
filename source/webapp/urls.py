from django.urls import path
from webapp.views import index, create_todo_list, todo_delete # noqa: F401

urlpatterns = [
    path('', index),
    path('create/', create_todo_list),
    path('delete/<int:id>/', todo_delete, name="delete")
]
