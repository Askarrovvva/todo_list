from django.shortcuts import render, redirect, get_object_or_404

from .models import Issue
from .forms import IssueForm


def index(request):
    issue = Issue.objects.order_by('-updated_at')
    return render(request, 'index.html', context={"issue": issue})


def create_issue(request):
    if request.method == "GET":
        form = IssueForm()
        return render(request, 'create_issue.html', context={"form": form})
    else:
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            return redirect('detail', pk=issue.pk)
        return render(request, "create_issue.html", {"form": form})




def delete_issue(request, *args, pk, **kwargs):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "GET":
        return render(request, "delete_issue.html", context={"issue": issue})
    else:
        if issue.statuses.title != "Done":
            return render(request, "delete_issue.html", context={"issue": issue, "error_message": "Удаление "
                                                            "запрещено! Задача должна быть выполнена (статус 'Done')."})
        issue.delete()
        return redirect("main")


def detail_issue(request, *args, pk, **kwargs):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, "detail_issue.html", context={"issue": issue})


def update_issue(request, *args, pk, **kwargs):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "GET":
        form = IssueForm(instance=issue)
        return render(request, "update_issue.html", context={"form": form})
    else:
        form = IssueForm(data=request.POST, instance=issue)
        if form.is_valid():
            issue = form.save()
            return redirect("detail", pk=issue.pk)
        return render(request, "update_issue.html", {"form": form})