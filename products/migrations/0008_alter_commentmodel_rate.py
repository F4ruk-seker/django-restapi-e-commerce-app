# Generated by Django 5.0.6 on 2024-06-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_commentmodel_is_name_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='rate',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
