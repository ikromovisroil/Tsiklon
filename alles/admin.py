from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Maxsulot)
class MaxsulotAdmin(admin.ModelAdmin):
    list_display = ('id','turi','nomi','soni','narxi','aksiya_n',)
    list_display_links = ('nomi',)
    list_filter = ('turi','nomi','soni',)
    search_fields = ('id','turi','nomi',)
    #dsfsdf
    #sddfsdfds

@admin.register(Turi)
class TuriAdmin(admin.ModelAdmin):
    list_display = ('id','nomi',)
