from django.urls import path
from .views import OrderListCreateView, OrderRetrieveUpdateDeleteView, ReceiptListCreateView, ReceiptRetrieveUpdateDeleteView

urlpatterns = [
    path('order', OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', OrderRetrieveUpdateDeleteView.as_view(), name='order-detail'),
    path('receipt', ReceiptListCreateView.as_view(), name='receipt-list-create'),
    path('receipt/<int:pk>/', ReceiptRetrieveUpdateDeleteView.as_view(), name='receipt-detail'),
]
