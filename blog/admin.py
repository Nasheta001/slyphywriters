from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'published_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at', 'published_at']
    fieldsets = (
        ('Content', {'fields': ('title', 'slug', 'category', 'author', 'featured_image', 'excerpt', 'content')}),
        ('Publishing', {'fields': ('status', 'published_at', 'created_at', 'updated_at')}),
    )
