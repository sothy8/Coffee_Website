from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Item, Invoice, InvoiceItem

def HomeView(request):
    return render(request, 'coffee/home.html')

def OrderView(request):
    items = Item.objects.all()
    return render(request, 'coffee/order.html', {'items': items})

def submit_order(request):
    if request.method == 'POST':
        invoice = Invoice.objects.create(seller_id=1, total_price=0)  # Set default total_price to 0
        for item in Item.objects.all():
            quantity_str = request.POST.get(f'quantity_{item.id}', '0')
            try:
                quantity = int(quantity_str)
            except ValueError:
                quantity = 0
            if quantity > 0:
                InvoiceItem.objects.create(
                    invoice=invoice,
                    item=item,
                    quantity=quantity,
                    unit_price=item.unit_price
                )
        invoice.total_price = sum(invoice_item.unit_price * invoice_item.quantity for invoice_item in invoice.items.all())
        invoice.save()
        return redirect(reverse('order_success', args=[invoice.id]))
    return redirect('order')

def OrderSuccessView(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice_items = InvoiceItem.objects.filter(invoice=invoice)
    order_items = [
        {'name': item.item.name, 'quantity': item.quantity, 'unit_price': item.unit_price}
        for item in invoice_items
    ]
    total_price = invoice.total_price
    
    return render(request, 'coffee/order_success.html', {
        'order_items': order_items,
        'total_price': total_price,
    })

def InvoiceDetailView(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice_items = InvoiceItem.objects.filter(invoice=invoice)
    return render(request, 'coffee/invoice_detail.html', {'invoice': invoice, 'invoice_items': invoice_items})