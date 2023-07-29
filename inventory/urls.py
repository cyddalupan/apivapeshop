from django.urls import path
from .views import InventoryListCreateView, InventoryRetrieveUpdateDeleteView

urlpatterns = [
    path('', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('<int:pk>/', InventoryRetrieveUpdateDeleteView.as_view(), name='inventory-detail'),
]