from django.contrib import admin

from firstProject.accounts.models import Profile
from firstProject.web.models import Category, Order, OrderItem, Product, user_model, ShippingAddress

admin.site.register(user_model)
admin.site.register(Profile)

admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
