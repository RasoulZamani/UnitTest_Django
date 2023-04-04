from django.contrib import admin
from .models import OtpCode

@admin.register(OtpCode)
class OptCodeAdmin(admin.ModelAdmin):
    list_display = ('phone','code', 'created')
