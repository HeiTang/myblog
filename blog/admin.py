from django.contrib import admin
from .models import Post,Tag,commodity

# Register your models here.

class TagInline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','text','created_date')
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

class commodityAdmin(admin.ModelAdmin):
    list_display = ('name','class_s','price','place','specification','created','token')
    fields = ('name','class_s','price','place','specification','created')
    search_fields = ('name',)


admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(commodity, commodityAdmin)