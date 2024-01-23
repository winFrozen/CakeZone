from django.contrib import admin
from .models import Aboutus, Contact, Menu, Team, Testimonial, Menu2, Menu3

# Register your models here.

admin.site.register(Aboutus)
admin.site.register(Contact)
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
@admin.register(Menu2)
class Menu2Admin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
@admin.register(Menu3)
class Menu3Admin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}