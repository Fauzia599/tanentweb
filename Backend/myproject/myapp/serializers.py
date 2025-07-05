from rest_framework import serializers
from .models import User, TentCategory, Event, Booking, Payment


# 1. User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# 2. Tent Category Serializer
class TentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TentCategory
        fields = '__all__'


# 3. Event Serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


# 4. Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='fullname', queryset=User.objects.all())
    tent_category = serializers.SlugRelatedField(slug_field='name', queryset=TentCategory.objects.all())
    event = serializers.SlugRelatedField(slug_field='title', queryset=Event.objects.all())

    class Meta:
        model = Booking
        fields = '__all__'


# 5. Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    booking = serializers.SlugRelatedField(slug_field='id', queryset=Booking.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'
