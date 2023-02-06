from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blog.models import User, Post, Commentary


@admin.register(User)
class PostAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name")}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "owner", "created_time"]
    list_filter = ["owner"]
    search_fields = ["title"]


@admin.register(Commentary)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "user", "created_time"]
    list_filter = ["user"]
    search_fields = ["post__title"]


admin.site.unregister(Group)
