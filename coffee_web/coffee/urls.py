from django.urls import path
from .views import HomeView, OrderView, submit_order, OrderSuccessView, InvoiceDetailView

urlpatterns = [
    path('', HomeView, name='home'),
    path('order/', OrderView, name='order'),
    path('order/submit/', submit_order, name='submit_order'),
    path('order/success/<int:invoice_id>/', OrderSuccessView, name='order_success'),
    path('invoice/<int:invoice_id>/', InvoiceDetailView, name='invoice_detail'),
]