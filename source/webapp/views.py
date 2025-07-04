from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import ToDo, status_choices

from webapp.forms import ToDoForm


def index(request):
    todos = ToDo.objects.order_by('-date_completion')
    return render(request, 'index.html', context={"todos": todos})


def todo_create(request):
    if request.method == "GET":
        form = ToDoForm()
        return render(request, 'todo_create.html', {"form": form})
    else:
        form = ToDoForm(request.POST)
        print(f"Form errors: {form.errors}")
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
        return render(request, 'todo_create.html', {"form": form})


def todo_update(request, *args, pk, **kwargs):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "GET":
        form = ToDoForm(instance=todo)
        return render(request, "todo_update.html", context={"form": form})
    else:
        form = ToDoForm(data=request.POST, instance=todo)
        print(f"Form errors: {form.errors}")
        if form.is_valid():
            todo = form.save()
            return redirect("todo_detail", pk=todo.pk)
        return render(request, "todo_update.html", {"form": form})



def todo_delete(request, *args, pk, **kwargs):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "GET":
        return render(request, "todo_delete.html", context={"todo": todo})
    else:
        todo.delete()
        return redirect("todo")


def todo_detail(request, *args, pk, **kwargs):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, "todo_detail.html", context={"todo": todo})