import logging

from django.db.models import ObjectDoesNotExist
from rest_framework import serializers

from .models import Product
from .models import Customer
from .models import PurchaseHistory

logger = logging.getLogger(__name__)


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class CustomerSerializersGet(serializers.ModelSerializer):
    username = serializers.CharField(source='login')


    class Meta:
        model = Customer
        fields = ['username', 'money_spent', ]


class CustomerSerializersPost(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['login', 'money_spent', ]


class PurchaseHistorySerializers(serializers.ModelSerializer):
    customer = CustomerSerializersPost()
    item = ProductSerializers()

    class Meta:
        model = PurchaseHistory
        fields = ('customer', 'item', "total", 'quantity', 'date')

    def create(self, validated_data: dict):

        product_name = validated_data.pop('item')
        customer_login: dict = validated_data.pop('customer')
        try:
            product = Product.objects.get(**product_name)
        except ObjectDoesNotExist:
            product = Product.objects.create(**product_name)

        try:
            customer = Customer.objects.get(login=customer_login['login'])
            customer.money_spent += validated_data['total']
            customer.save()
        except ObjectDoesNotExist:
            customer = Customer.objects.create(**customer_login)
        if product is not customer.stone.all():
            customer.stone.add(product)
            customer.save()

        return PurchaseHistory.objects.create(customer=customer, item=product, **validated_data)
