from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'category', 'birthday', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le numéro de téléphone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'email'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Entrez l\'adresse'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'phone_number': 'Téléphone',
            'email': 'Email',
            'address': 'Adresse',
            'category': 'Catégorie',
            'birthday': 'Date de naissance',
            'image': 'Photo',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Vérification du format du numéro de téléphone
        if not re.match(r'^\+?[\d\s-]{8,}$', phone_number):
            raise forms.ValidationError('Veuillez entrer un numéro de téléphone valide')
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Vérification si l'email existe déjà
        if Contact.objects.filter(email=email).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise forms.ValidationError('Cet email est déjà utilisé par un autre contact')
        return email 