from django.shortcuts import render, redirect
from django.contrib import messages
from .models import QuoteRequest, ContactMessage


def about(request):
    team = [
        {'icon': '✍️', 'name': 'Alex K.', 'role': 'Lead Content Writer'},
        {'icon': '📊', 'name': 'Maria S.', 'role': 'SEO Strategist'},
        {'icon': '🌍', 'name': 'David O.', 'role': 'Translations Lead'},
        {'icon': '🔗', 'name': 'Sophie R.', 'role': 'Link Building Expert'},
        {'icon': '🎯', 'name': 'James P.', 'role': 'Crypto Specialist'},
        {'icon': '🚀', 'name': 'Lucia M.', 'role': 'iGaming Writer'},
    ]
    return render(request, 'core/about.html', {'team': team})

def process(request):
    return render(request, 'core/process.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        msg = request.POST.get('message', '').strip()
        if name and email and subject and msg:
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=msg)
            messages.success(request, "Message sent! We'll get back to you within 24 hours.")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all fields.")
    return render(request, 'core/contact.html')

def quote(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        company = request.POST.get('company', '').strip()
        website = request.POST.get('website', '').strip()
        service = request.POST.get('service', '').strip()
        industry = request.POST.get('industry', '').strip()
        volume = request.POST.get('volume', '').strip()
        msg = request.POST.get('message', '').strip()
        if name and email and service and industry and msg:
            QuoteRequest.objects.create(
                name=name, email=email, company=company, website=website,
                service=service, industry=industry, volume=volume, message=msg
            )
            messages.success(request, "Quote request received! Our team will contact you within 24 hours.")
            return redirect('quote')
        else:
            messages.error(request, "Please fill in all required fields.")
    return render(request, 'core/quote.html')

# Services
def service_seo_content(request):
    return render(request, 'core/services/seo_content.html')

def service_seo_services(request):
    return render(request, 'core/services/seo_services.html')

def service_translation(request):
    return render(request, 'core/services/translation.html')

def service_editing(request):
    return render(request, 'core/services/editing.html')

def service_link_building(request):
    return render(request, 'core/services/link_building.html')

# Industries
def industry_igaming(request):
    return render(request, 'core/industries/igaming.html')

def industry_fintech(request):
    return render(request, 'core/industries/fintech.html')

def industry_crypto(request):
    return render(request, 'core/industries/crypto.html')

# Override home to pass steps context
def home(request):
    steps = [
        ('1', 'Reviewing Your Order', 'Tell us what you need and set deadlines'),
        ('2', 'Matching You With Experts', 'We assign the right specialist for your task'),
        ('3', 'Collaboration & Feedback', 'Stay in the loop with progress updates'),
        ('4', 'Final Quality Checks', 'Multiple reviews before delivery'),
    ]
    return render(request, 'core/home.html', {'steps': steps})
