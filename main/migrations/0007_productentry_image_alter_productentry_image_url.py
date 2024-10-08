# Generated by Django 5.1.1 on 2024-10-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_productentry_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='productentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='productentry',
            name='image_url',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
    ]
