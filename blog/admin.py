from django.contrib import admin
from .models import Post
from users.models import Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at') 
    search_fields = ('title',)  

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')  # Adjust this to display the fields you want
    search_fields = ('user__username', 'bio')