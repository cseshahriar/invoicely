from django.shortcuts import render
from rest_framework import viewsets

from .serializers import InvoiceSerializer, ItemSerializer
from django.core.exceptions import PermissionDenied

from .models import Invoice, Item


class InvoiceViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        team = self.request.user.teams.all()
        serializer.save(created_by=self.request.user, team=team)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')

        serializer.save()


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        invoice_id = self.request.GET.get('invoice_id', 0)
        return self.queryset.filter(invoice__id=invoice_id)