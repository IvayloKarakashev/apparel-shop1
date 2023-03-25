import datetime
import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from firstProject.accounts.models import Profile

user_model = get_user_model()


class Category(models.Model):
    TITLE_MAX_LENGTH = 25
    TYPE_MAX_LENGTH = 1

    MEN = 'M'
    WOMEN = 'F'
    CHILDREN = 'C'

    TYPE_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (CHILDREN, 'Children')
    ]

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=TYPE_CHOICES
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    TITLE_MAX_LENGTH = 25
    COLOR_MAX_LENGTH = 25

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

    image = models.ImageField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    uploaded_by = models.ForeignKey(user_model, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.image:
            filename = slugify(self.image.name.replace(' ', '_'))
            self.image.name = filename

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductSize(models.Model):
    SIZE_NAME_MAX_LENGTH = 10

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=SIZE_NAME_MAX_LENGTH
    )

    def __str__(self):
        return f"{self.name} - {self.product}"


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
    RECIPIENT_FIRST_NAME_MAX_LENGTH = 30
    RECIPIENT_LAST_NAME_LENGTH = 30
    RECIPIENT_PHONE_NUMBER_MAX_LENGTH = 14

    profile = models.ForeignKey(  # Should be user ?
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    recipient_first_name = models.CharField(
        max_length=RECIPIENT_FIRST_NAME_MAX_LENGTH,
        verbose_name='First name'
    )

    recipient_last_name = models.CharField(
        max_length=RECIPIENT_LAST_NAME_LENGTH,
        verbose_name='Last name'
    )

    recipient_phone_number = models.CharField(
        max_length=RECIPIENT_PHONE_NUMBER_MAX_LENGTH,
        verbose_name='Phone number'
    )

    state_region = models.CharField(
        max_length=STATE_REGION_MAX_LENGTH,
        null=True,
        verbose_name='State/Region'
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

    label = models.CharField(
        max_length=LABEL_MAX_LENGTH,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Shipping addresses'


class Order(models.Model):
    customer = models.ForeignKey(
        user_model,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date_ordered = models.DateTimeField(
        auto_now_add=True
    )
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

    shipping_fee = models.FloatField(
        default=4.00
    )

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_subtotal(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        return self.get_cart_subtotal + self.shipping_fee

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_expected_delivery_date(self):
        return self.date_ordered + datetime.timedelta(days=3)


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

    size = models.ForeignKey(
        ProductSize,
        on_delete=models.SET_NULL,
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


class FAQ(models.Model):
    question = models.TextField()

    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['id']
