# Generated by Django 5.1 on 2024-09-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_productentry_difficulty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productentry',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Difficult', 'Difficult')], default='Easy', max_length=10),
        ),
    ]
