from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'thumbnail',
            'price',
            'stock',
            'size',
            'team',
            'is_featured',
        ]
