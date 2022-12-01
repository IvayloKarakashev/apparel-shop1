from django.contrib import admin
from django.contrib.admin import TabularInline

from firstProject.accounts.models import Profile
from firstProject.web.models import Category, Order, OrderItem, Product, ProductSize, user_model, ShippingAddress, FAQ


class SizeInLine(TabularInline):
    model = ProductSize


class ProductAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(uploaded_by=request.user)

    exclude = ('uploaded_by',)

    inlines = [
        SizeInLine,
    ]

    def save_model(self, request, obj, form, change):
        obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)

# admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(Category)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

admin.site.register(FAQ)
