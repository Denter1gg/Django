from django.contrib import admin
from .models import *


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "task", "title"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "author", "date_of_staging", "title"]

class TagsAdmin(admin.ModelAdmin):
    list_display = ["id", "tags", ]


admin.site.register(Task, TaskAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagsAdmin)