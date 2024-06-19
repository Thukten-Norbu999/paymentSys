from rest_framework import serializers

from useraccount.models import CustomUser, Account

class UserSerializers(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = []

class Account(serializers.Serializer):
    class Meta:
        model = Account
        fields = []
