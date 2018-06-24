from django.contrib import admin
from genealogy_app.models import Anceator, Family

# Register your models here.

@admin.register(Anceator)
class AnceatorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname')

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('family_name',)

