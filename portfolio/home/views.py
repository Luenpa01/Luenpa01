from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
   return render(request, 'home.html')

def about(request):
   return render(request, 'about.html')

def project(request):
   return render(request, 'project.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')
