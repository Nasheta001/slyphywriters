from django.contrib import admin
from .models import QuoteRequest, ContactMessage

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'service', 'industry', 'created_at', 'is_read']
    list_filter = ['service', 'industry', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'company']
    list_editable = ['is_read']
    readonly_fields = ['created_at']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
