from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from reports.serializers import ReportOutputSerializer

from .models import Report


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20


class ReportRetrieveView(APIView):

    def get(self, request):
        query = Report.objects.all()
        params = request.GET
        date_from, date_to = params.get("date_from"), params.get("date_to")
        if date_from and date_to:
            query.filter(report_date__gte=date_from, report_date__lte=date_to)

        paginator = CustomPageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(query, request)
        response = ReportOutputSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(response.data)


class ReportRetrieveViewTest(ListAPIView):
    """
    Я, в своих проектах, не использую дженерики, по типу ListApiView, ListCreateApiView и подобные, для большего
    контроля. Написал для справки, что бы было понимание, что я знаю про их существование =)
    """
    pagination_class = CustomPageNumberPagination
    serializer_class = ReportOutputSerializer

    def get_queryset(self):
        query = Report.objects.all()
        params = self.request.GET
        date_from, date_to = params.get("date_from"), params.get("date_to")
        if date_from and date_to:
            query.filter(report_date__gte=date_from, report_date__lte=date_to)

        return query
