from rest_framework import serializers
from .models import Menu, Booking

class BookingSerializers(serializers.Serializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuSerializers(serializers.Serializer):
    class Meta:
        model = Menu
        fields = '__all__'