# Generated by Django 4.2.4 on 2024-05-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_category_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='brand',
        ),
    ]
