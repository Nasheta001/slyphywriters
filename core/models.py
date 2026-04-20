from django.db import models


class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('seo_content', 'SEO Content Writing'),
        ('seo_services', 'SEO Services'),
        ('translation', 'Translation'),
        ('editing', 'Editing'),
        ('link_building', 'Link Building'),
        ('other', 'Other / Multiple'),
    ]
    INDUSTRY_CHOICES = [
        ('igaming', 'iGaming'),
        ('fintech', 'Fintech'),
        ('crypto', 'Crypto'),
        ('other', 'Other'),
    ]
    VOLUME_CHOICES = [
        ('small', 'Small (1–5 pieces)'),
        ('medium', 'Medium (6–20 pieces)'),
        ('large', 'Large (20+ pieces)'),
        ('ongoing', 'Ongoing retainer'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    volume = models.CharField(max_length=20, choices=VOLUME_CHOICES, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.get_service_display()}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"
