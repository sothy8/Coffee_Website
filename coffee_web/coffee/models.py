from django.db import models
from datetime import date

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    activation = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.id} {self.name}"
    
    
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', default=1)
    name = models.CharField(max_length=100)
    unit_price = models.FloatField()
    activation = models.BooleanField(default=True)
    image_name = models.CharField(max_length=100, blank=True, null=True)  # Use image_name instead of image_url  
    
    def __str__(self):
        return f"{self.id} {self.name} {self.unit_price}"
    
class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    activation = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.id} {self.name} {self.address}"
    
class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='seller', default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    activation = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email}"

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='invoices', default=1)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='invoices', default=1)
    total_price = models.FloatField()
    activation = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Invoice {self.id} on {self.date}"
    
    def create_order(self, items):
        for item, quantity in items:
            InvoiceItem.objects.create(
                invoice=self,
                item=item,
                quantity=quantity,
                unit_price=item.unit_price
            )
        self.total_price = sum(item.unit_price * quantity for item, quantity in items)
        self.save()

class InvoiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='invoice_items', default=1)
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0.0)
    activation = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.unit_price = self.item.unit_price
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"InvoiceItem {self.id} for {self.item.name}"