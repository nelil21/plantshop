# Generated by Django 5.1.1 on 2024-10-07 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_productentry_image_alter_productentry_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productentry',
            name='image_url',
        ),
    ]
