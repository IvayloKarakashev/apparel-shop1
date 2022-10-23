from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse, reverse_lazy

User = get_user_model()


class Category(models.Model):
    TITLE_MAX_LENGTH = 25

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    TITLE_MAX_LENGTH = 25
    SIZE_MAX_LENGTH = 10  # Choices ?
    COLOR_MAX_LENGTH = 25

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    size = models.CharField(
        max_length=SIZE_MAX_LENGTH,
    )

    color = models.CharField(
        max_length=COLOR_MAX_LENGTH,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(0.1)
        ]
    )

    image = models.URLField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)

    # date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
