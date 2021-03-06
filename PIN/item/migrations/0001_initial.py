# Generated by Django 3.2.5 on 2021-07-14 20:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created by')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified by')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('exist_deleted', models.BooleanField(default=True, help_text='If True the item exists. If it is False the item has been deleted.', verbose_name='exists/deleted')),
                ('description', models.TextField(verbose_name='Description')),
                ('base_price', models.FloatField(verbose_name='base_price')),
                ('sold_price', models.FloatField(verbose_name='sold_price')),
                ('status', models.CharField(max_length=50, verbose_name='status')),
                ('bid_start_date', models.DateTimeField(verbose_name='bid_start_date')),
                ('bid_end_date', models.DateTimeField(verbose_name='bid_end_date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
