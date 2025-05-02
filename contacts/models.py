from django.db import models

# Create your models here.

class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('FAV', 'Favoris'),
        ('FAM', 'Famille'),
        ('FRI', 'Amis'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(blank=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='FRI')
    birthday = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='contacts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['last_name', 'first_name']
