from django.contrib import admin
from .models import Post

# Register your models here.


#Model Admin
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Post, PostAdmin)
