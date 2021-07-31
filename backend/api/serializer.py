from rest_framework import serializers

from .models import PurchaseHistory

class SerializersPurchaseHistoryCreate(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = ('customer', 'product', "total", 'quantity', 'date')
