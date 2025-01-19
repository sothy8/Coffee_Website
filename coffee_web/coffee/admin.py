from django.contrib import admin
from .models import Category, Item, Branch, Seller, Invoice, InvoiceItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'activation')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit_price', 'activation')

class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'activation')

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'activation')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'branch', 'seller', 'total_price', 'activation')

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'item', 'quantity', 'unit_price', 'activation')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
