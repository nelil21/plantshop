from django.db import models
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import User

class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=100, blank=True)
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Difficult', 'Difficult'),
    ]
    
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')

    def save(self, *args, **kwargs):
        self.image_url = f"{slugify(self.name)}.png"  # Pastikan ekstensi sesuai dengan file yang ada
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
