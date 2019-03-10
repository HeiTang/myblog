from django.contrib import admin
from .models import Post,Tag

# Register your models here.

class TagInline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','text','created_date')
    # fields  = ('title', 'text','published_date')
    search_fields = ('title',)
    inlines = [TagInline]
    fieldsets = (
        ['Main',{
            'fields':('title','text'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('created_date',),
        }]
 
    )

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)