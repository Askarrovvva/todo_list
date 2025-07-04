from django.urls import path
from webapp.views import index, todo_create, todo_detail, todo_delete, todo_update   # noqa: F401

urlpatterns = [
    path('', index, name='todo'),
    path('create/', todo_create, name='todo_create'),
    path('todo/<int:pk>/', todo_detail, name="todo_detail"),
    path('update/<int:pk>/', todo_update, name="todo_update"),
    path('delete/<int:pk>/', todo_delete, name="todo_delete"),
]

