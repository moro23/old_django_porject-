import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    prince = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[str(self.id), self.slug])