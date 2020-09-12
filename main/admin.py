from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    fields = ('name', 'birthday', 'photo', 'description', 'parent1', 'parent2', 'sale')

@admin.register(Cat_Photo)
class CatPhotoAdmin(admin.ModelAdmin):
    fields = ('fk_cat', 'image')
