from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='ebooks/')
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except AttributeError:
            url = ''
        return url
