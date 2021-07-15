from django.db import models
from django.urls import reverse_lazy

from PIN.core.models import (
    Active,
    Address,
    Document,
    TimeStampedModel,
    UuidModel
)


class Person(UuidModel, TimeStampedModel, Address, Document, Active):
    first_name = models.CharField('name', max_length=50)
    last_name = models.CharField('last name', max_length=50, null=True, blank=True)  # noqa E501
    email = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'person'
        verbose_name_plural = 'persons'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name or ""}'.strip()

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse_lazy('category:person_detail', kwargs={'pk': self.pk})
