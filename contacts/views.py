from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.core.paginator import Paginator
from django.db import models
from django.core.exceptions import ValidationError

def contact_list(request):
    search_query = request.GET.get('search', '')
    contacts = Contact.objects.all()
    
    if search_query:
        contacts = contacts.filter(
            models.Q(first_name__icontains=search_query) |
            models.Q(last_name__icontains=search_query)
        )
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'contacts/contact_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                contact = form.save()
                messages.success(request, f'Le contact {contact.first_name} {contact.last_name} a été créé avec succès!')
                return redirect('contacts:contact_list')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'Erreur dans le champ {field}: {error}')
        except ValidationError as e:
            messages.error(request, str(e))
    else:
        form = ContactForm()
    
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': 'Nouveau contact'
    })

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        try:
            if form.is_valid():
                contact = form.save()
                messages.success(request, f'Le contact {contact.first_name} {contact.last_name} a été mis à jour avec succès!')
                return redirect('contacts:contact_detail', pk=contact.pk)
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'Erreur dans le champ {field}: {error}')
        except ValidationError as e:
            messages.error(request, str(e))
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': f'Modifier {contact.first_name} {contact.last_name}'
    })

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact supprimé avec succès!')
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
