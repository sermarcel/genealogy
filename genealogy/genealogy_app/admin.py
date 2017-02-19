from django.contrib import admin
from genealogy_app.models import Anceator, Relationship

# Register your models here.

@admin.register(Anceator)
class AnceatorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname')

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('relation_name',)

