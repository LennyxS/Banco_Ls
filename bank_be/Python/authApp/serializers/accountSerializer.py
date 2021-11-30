from django.db.models       import fields
from authApp.models.account import Account
from rest_framework         import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Account
        fields = ['balance', 'lastChangeDate', 'isActive']
 

