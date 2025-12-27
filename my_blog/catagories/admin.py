from django.contrib import admin
from .models import Catagory

# Register your models here.
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    list_filter = ('name', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Catagory, CatagoryAdmin)