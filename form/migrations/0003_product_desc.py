
# Generated by Django 5.2.1 on 2025-05-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
