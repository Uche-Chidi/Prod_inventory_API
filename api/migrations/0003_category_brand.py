# Generated by Django 4.2.4 on 2024-05-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_products_category_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='brand',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
