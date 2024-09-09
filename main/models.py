from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Nama tanaman
    price = models.IntegerField()  # Harga tanaman
    description = models.TextField()  # Deskripsi tanaman
    stock = models.IntegerField(default=0)  # Stok tanaman
    difficulty = models.CharField(
        max_length=20, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Medium'
    )  # Tingkat perawatan
    image_url = models.URLField(null=True, blank=True)  # URL gambar tanaman

    def __str__(self):
        return self.name
