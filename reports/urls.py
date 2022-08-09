from django.urls import path

from reports.views import ReportRetrieveView, ReportRetrieveViewTest

urlpatterns = [
    path("", ReportRetrieveView.as_view(), name="reports-retrieve"),
    path("test/", ReportRetrieveViewTest.as_view(), name="reports-retrieve")
]
