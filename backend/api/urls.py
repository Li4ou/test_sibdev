from django.urls import path

from .views import CsvViewsFiles
from .views import CustomerView

urlpatterns = [
    path('post/', CsvViewsFiles.as_view({'post': 'create'})),
    path('get/', CustomerView.as_view())
]
