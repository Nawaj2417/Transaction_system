from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'name', 'phone', 'email', 'transaction_date', 'status')
    search_fields = ('transaction_id', 'name', 'phone', 'email')