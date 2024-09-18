import uuid
from django.db import models

class ProductEntry(models.Model):
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
