from django.contrib import admin

from firstProject.accounts.models import Profile
from firstProject.web.models import Category, Order, OrderItem, Product, ProductSize, user_model, ShippingAddress, FAQ

admin.site.register(user_model)
admin.site.register(Profile)

admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(Category)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

admin.site.register(FAQ)
