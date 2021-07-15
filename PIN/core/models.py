import uuid

from django.contrib.auth.models import User
from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class UuidModel(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'created by',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modified by',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class CreatedBy(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name='created by',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(
        'address',
        max_length=100,
        null=True,
        blank=True
    )
    address_number = models.IntegerField('número', null=True, blank=True)
    complement = models.CharField(
        'complement',
        max_length=100,
        null=True,
        blank=True
    )
    district = models.CharField(
        'district',
        max_length=100,
        null=True,
        blank=True
    )
    city = models.CharField('cidade', max_length=100, null=True, blank=True)
    uf = models.CharField(
        'UF',
        max_length=2,
        choices=STATE_CHOICES,
        null=True,
        blank=True
    )
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)
    country = models.CharField(
        'country',
        max_length=50,
        default='Pakistan',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'address': self.address,
            'address_number': self.address_number,
            'complement': self.complement,
            'district': self.district,
            'city': self.city,
            'uf': self.uf,
            'cep': self.cep,
        }


class Document(models.Model):
    cpf = models.CharField(
        'CPF',
        max_length=11,
        unique=True,
        null=True,
        blank=True
    )
    rg = models.CharField('RG', max_length=11, null=True, blank=True)
    cnh = models.CharField('CNH', max_length=20, null=True, blank=True)

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'cpf': self.cpf,
            'rg': self.rg,
            'cnh': self.cnh,
        }


class Active(models.Model):
    active = models.BooleanField('active', default=True)
    exist_deleted = models.BooleanField(
        'exists/deleted',
        default=True,
        help_text='If True the item exists. If it is False the item has been deleted.'
    )

    class Meta:
        abstract = True
