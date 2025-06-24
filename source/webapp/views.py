from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.models import ToDo, status_choices  # noqa: F401


def index(request):
    todos = ToDo.objects.order_by('-date_completion')
    return render(request, 'index.html', context={"todos": todos})



def create_todo_list(request):
    if request.method == "GET":
        return render(request, "create_todo_list.html", {"status_choices": status_choices})  # убрано webapp/
    else:
        date_completion = request.POST.get("date_completion")
        if date_completion == '':
            date_completion = None

        ToDo.objects.create(
            description=request.POST.get("description"),
            status=request.POST.get("status"),
            date_completion=date_completion
        )
        return HttpResponseRedirect("/")


def todo_delete(request, id):
    try:
        todo = ToDo.objects.filter(id=id)
        todo.delete()
        return HttpResponseRedirect("/")
    except ToDo.DoesNotExist:
        return HttpResponseRedirect("/")

