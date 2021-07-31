from django.shortcuts import render
from rest_framework import viewsets

from .serializer import SerializersPurchaseHistoryCreate


# TODO Написание views для обработки фалов
class CsvViewsFiles(viewsets.ModelViewSet):
    """ """
    serializer_class = SerializersPurchaseHistoryCreate


# Create your views here.
