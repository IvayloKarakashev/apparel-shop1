from django.db import models


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

    image = models.URLField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
