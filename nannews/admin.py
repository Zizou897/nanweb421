from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "date_add", "status")
    date_hierarchy = "date_add" 
    list_editable = ["status"]


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "image_view", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("nom_site","image_view","address", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"



@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("telephone", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]



@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("nom", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]

@admin.register(models.SocialUser)
class SocialUserAdmin(admin.ModelAdmin):
    list_display = ("link", "social", "team", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]

@admin.register(models.Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ("nom_history", "titre_description", "date_add", "status")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["status"]