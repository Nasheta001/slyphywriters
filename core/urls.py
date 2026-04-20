from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('process/', views.process, name='process'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('quote/', views.quote, name='quote'),
    # Services
    path('services/seo-content-writing/', views.service_seo_content, name='service_seo_content'),
    path('services/seo-services/', views.service_seo_services, name='service_seo_services'),
    path('services/translation/', views.service_translation, name='service_translation'),
    path('services/editing/', views.service_editing, name='service_editing'),
    path('services/link-building/', views.service_link_building, name='service_link_building'),
    # Industries
    path('industry/igaming/', views.industry_igaming, name='industry_igaming'),
    path('industry/fintech/', views.industry_fintech, name='industry_fintech'),
    path('industry/crypto/', views.industry_crypto, name='industry_crypto'),
]
