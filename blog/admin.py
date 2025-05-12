from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

    search_fields = ('title', 'content')

    list_filter = ('title',)

    ordering = ('-id',)

admin.site.register(Post, PostAdmin)
