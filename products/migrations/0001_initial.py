# Generated by Django 5.0.6 on 2024-06-11 00:23

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('H', 'HIDE'), ('S', 'SHOW')], max_length=1)),
                ('title', models.CharField(max_length=30)),
                ('keyword', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('item_type', models.CharField(choices=[('P', 'PHYSICAL'), ('v', 'VIRTUAL')], default='P', max_length=1)),
                ('status', models.CharField(choices=[('D', 'DELETE'), ('H', 'HIDE'), ('S', 'SHOW')], default='True', max_length=1)),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('keyword', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('amount', models.IntegerField(default=0)),
                ('details', models.TextField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('title', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(blank=True, default=None, to='products.productmodel')),
            ],
        ),
    ]
