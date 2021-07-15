from django.db import models
from django.urls import reverse_lazy

from PIN.category.models import Category
from PIN.core.models import (
    Active,
    TimeStampedModel,
    UuidModel
)


class Item(UuidModel, TimeStampedModel, Active):
    title = models.CharField('title', max_length=50)
    description = models.TextField('description')
    base_price = models.FloatField('base_price')
    sold_price = models.FloatField('sold_price')
    status = models.CharField('status', max_length=50)
    bid_start_date = models.DateTimeField('bid_start_date')
    bid_end_date = models.DateTimeField('bid_end_date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    class Meta:
        pass
        ordering = (  'base_price', 'sold_price')
        # verbose_name = 'category'
        # verbose_name_plural = 'categories'

    # @property
    # def item_title(self):
    #     return f'{self.item_title}'.strip()
    #
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse_lazy('item:item_detail', kwargs={'pk': self.pk})
