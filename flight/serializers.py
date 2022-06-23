from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
        )

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    passenger = PassengerSerializer(many=True, required=False)
    serializer = serializers.StringRelatedField() #default read_only = True
    user = serializers.StringRelatedField() #default read_only = True
    flight_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only = True, required = False)


    class Meta :
        model = Reservation
        fields = (
            'id',
            'flight',
            'user',
            'passenger',
        )
