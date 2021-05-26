from django.shortcuts import render
from rest_framework import viewsets

from .serializers import InvoiceSerializer
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