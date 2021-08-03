import logging

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .serializer import PurchaseHistorySerializers
from .serializer import CustomerSerializers
from .parsers import CSVTextParser
from .models import Customer

# Create your views here.
logger = logging.getLogger(__name__)


class CsvViewsFiles(ModelViewSet):
    parser_classes = [CSVTextParser]
    serializer_class = PurchaseHistorySerializers

    def create(self, request, *args, **kwargs):
        serializer: PurchaseHistorySerializers = self.get_serializer(data=request.data,
                                                                     many=isinstance(request.data, list))
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'status': 'ok'}, status=status.HTTP_200_OK, headers=headers)

        return Response({'Status': 'Error', 'Desc': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CustomerView(ListAPIView):
    serializer_class = CustomerSerializers
    queryset = Customer.objects.all()[:5]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        serializer = self.adding_gems_list_to_data(queryset, serializer)

        return Response({"response": serializer.data})

    def adding_gems_list_to_data(self, queryset, serializer):
        """gems - список из названий камней, которые купили
         как минимум двое из списка "5 клиентов,потративших
          наибольшую сумму за весь период", и данный клиент
           является одним из этих покупателей."""

        for index, customer in enumerate(queryset):
            gems_set = set()
            for s in queryset:
                if s.id != customer.id:
                    for stone in s.stone.all():
                        gems_set.add(stone.name)
            gems = set(name.name for name in customer.stone.all()).intersection(gems_set)

            serializer.data[index]['gems'] = gems

        return serializer
