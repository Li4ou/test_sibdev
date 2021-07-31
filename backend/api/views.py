from django.shortcuts import render

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import SerializersPurchaseHistoryCreate
from .parsers import CSVTextParser


# Create your views here.


class CsvViewsFiles(viewsets.ModelViewSet):
    parser_classes = [CSVTextParser]
    serializer_class = SerializersPurchaseHistoryCreate

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid()
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'status': 'ok'}, status=status.HTTP_200_OK, headers=headers)

        return Response({'Status': 'Error', 'Desc':serializer.errors}, status=status.HTTP_400_BAD_REQUEST )




