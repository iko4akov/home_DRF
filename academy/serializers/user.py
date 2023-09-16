from rest_framework import serializers

from academy.serializers import PaySerializer
from user.models import User


class UserPaySerializer(serializers.ModelSerializer):
    pay = PaySerializer(source='pay_set', many=True)
    class Meta:
        model = User
        fields = ('email', 'pay')
