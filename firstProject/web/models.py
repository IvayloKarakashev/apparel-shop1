import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from firstProject.accounts.models import Profile

user_model = get_user_model()


class Category(models.Model):
    TITLE_MAX_LENGTH = 25

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image = models.ImageField()

    def __str__(self):
        return self.title


class Product(models.Model):
    TITLE_MAX_LENGTH = 25
    SIZE_MAX_LENGTH = 5
    COLOR_MAX_LENGTH = 25

    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    XXL = 'XXL'
    XXXL = 'XXXL'
    XXXXL = 'XXXXL'

    SIZE_CHOICES = [
        (XS, 'XS'),
        (S, 'S'),
        (M, 'M'),
        (L, 'L'),
        (XL, 'XL'),
        (XXL, 'XXL'),
        (XXXL, 'XXXL'),
        (XXXXL, 'XXXXL')
    ]

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    color = models.CharField(
        max_length=COLOR_MAX_LENGTH,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(0.1)
        ]
    )

    size = models.CharField(
        max_length=SIZE_MAX_LENGTH,
        choices=SIZE_CHOICES
    )

    image = models.ImageField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class WishList(models.Model):
    user = models.ForeignKey(
        user_model,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    date_added = models.DateTimeField(
        auto_now_add=True
    )


class ShippingAddress(models.Model):
    ADDRESS_MAX_LENGTH = 200
    CITY_MAX_LENGTH = 100
    STATE_REGION_MAX_LENGTH = 100
    LABEL_MAX_LENGTH = 20

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    state_region = models.CharField(
        max_length=STATE_REGION_MAX_LENGTH,
        null=True
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        null=True
    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LENGTH,
        null=True)

    zip_code = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    date_added = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.address


class Order(models.Model):
    customer = models.ForeignKey(
        user_model,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # date_created = models.DateTimeField(
    #     auto_now_add=True
    # )
    #
    # date_ordered = models.DateTimeField(
    #     auto_now=True
    # )

    complete = models.BooleanField(
        default=False

    )

    transaction_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        db_index=True,
        editable=False
    )

    shipping_address = models.ForeignKey(
        ShippingAddress,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

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
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,  # ?
        blank=True,
        null=True
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    quantity = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )

    date_added = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
