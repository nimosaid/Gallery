from django.contrib import admin
from .models import Photographer,Photo,Location
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Photographer)
admin.site.register(Photo)
admin.site.register(Location)