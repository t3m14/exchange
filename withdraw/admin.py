from django.contrib import admin
from .models import Transaction
class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('wallet','rdw')  # Contain only fields in your `custom-user-model`
admin.site.register(Transaction, TransactionAdmin)