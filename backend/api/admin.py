from django.contrib import admin

from .models import PurchaseHistory
from .models import Customer
from .models import Product

# Register your models here.

admin.site.register(PurchaseHistory)
admin.site.register(Customer)
admin.site.register(Product)

