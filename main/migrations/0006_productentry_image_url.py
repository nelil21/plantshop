# Generated by Django 5.1 on 2024-10-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_productentry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='productentry',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]