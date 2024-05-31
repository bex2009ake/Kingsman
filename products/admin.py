from django.contrib import admin
from products.models import *
# Register your models here.



admin.site.register(ProductImg)
admin.site.register(ProductVideo)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(CashbackHistory)
admin.site.register(Order)