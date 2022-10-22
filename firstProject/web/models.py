from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

user_model = get_user_model()


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


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
