from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        read_only_fields = ('created_by', 'created_at',)
        fields = (
            'id', 
            'name',
            'email',
            'org_number',
            'address1',
            'address2',
            'zipcode',
            'place',
            'country',
            'contact_person',
            'contact_reference'
        )
