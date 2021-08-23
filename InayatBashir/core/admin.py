from django.contrib import admin
from . import models


class CategoryBlog(admin.ModelAdmin):
    model = models.Blog
    fields = ( 'name', 'description', 'image_one', 'image_two',  'is_in_top_three','is_top_one')
    read_only_fields = ('id',)
 
admin.site.register(models.Blog)
admin.site.register(models.City)
admin.site.register(models.Places)


