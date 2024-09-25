import uuid
from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
=======

class ProductEntry(models.Model):
>>>>>>> 1a7b03bd959b9151ffe716a38f1fd4426c2927f1
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)  # Nama tanaman
    price = models.IntegerField()  # Harga tanaman
    description = models.TextField()  # Deskripsi tanaman
    stock = models.IntegerField()  # Stok tanaman
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Difficult', 'Difficult'),
    ]
    
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')