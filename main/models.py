import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)            # nama jersey
    content = models.TextField()                        # deskripsi jersey
    thumbnail = models.URLField(blank=True, null=True)  # gambar jersey
    price = models.IntegerField()                       # harga jersey
    stock = models.IntegerField(default=0)              # stok jersey
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    team = models.CharField(max_length=100)             # nama tim (contoh: MU, Madrid, Persija)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)    # ditampilkan sebagai produk unggulan
    product_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team} - {self.title}"
    
    @property
    def is_product_hot(self):
        return self.product_views > 20

    def increment_views(self):
        self.product_views += 1
        self.save()