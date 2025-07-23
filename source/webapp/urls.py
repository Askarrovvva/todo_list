from django.urls import path
from webapp.views.issues import IssueListView, CreateIssueView, IssueDetailView, DeleteIssueView, UpdateIssueView


urlpatterns = [
    path('', IssueListView.as_view(), name='main'),
    path('issue/create/', CreateIssueView.as_view(), name='create'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name="detail"),
    path('issue/<int:pk>/update/', UpdateIssueView.as_view(), name='update'),
    path('issue/<int:pk>/delete/', DeleteIssueView.as_view(), name='delete')
]