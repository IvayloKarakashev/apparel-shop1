from django.contrib import admin

from firstProject.accounts.models import Profile
from firstProject.web.models import Product, OrderItem, Order, User

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
