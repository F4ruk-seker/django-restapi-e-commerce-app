# Generated by Django 5.0.6 on 2024-06-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='row',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
