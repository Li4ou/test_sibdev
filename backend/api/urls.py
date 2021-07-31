from django.urls import path

from .views import CsvViewsFiles
#TODO Написание эндпоинтов для Get и Post
urlpatterns = [
    path('/post', CsvViewsFiles.as_view({'post':'create'}))
]
