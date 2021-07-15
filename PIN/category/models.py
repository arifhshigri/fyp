from django.db import models
from django.urls import reverse_lazy

from PIN.core.models import (
    Active,
    TimeStampedModel,
    UuidModel
)


class Category(UuidModel, TimeStampedModel, Active):
    cat_name = models.CharField('name', max_length=50)

    class Meta:
        ordering = ('cat_name',)
        # verbose_name = 'category'
        # verbose_name_plural = 'categories'

    @property
    def name(self):
        return f'{self.cat_name}'.strip()

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse_lazy('category:category_detail', kwargs={'pk': self.pk})
