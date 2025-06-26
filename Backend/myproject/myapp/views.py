from .models import User, TentCategory, Event, Booking, Payment # type: ignore
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, TentCategorySerializer, EventSerializer, BookingSerializer, PaymentSerializer # type: ignore
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def api(request, id=None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many=True)
                return Response(serializer.data)

        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})

        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'})
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
            else:
             return Response({'error': 'ID is required for DELETE method'}, status=400)
    return api

# 📌 Hizi ndiyo views zako sasa
manage_user = generic_api(User, UserSerializer)
manage_tent = generic_api(TentCategory, TentCategorySerializer)
manage_event = generic_api(Event, EventSerializer)
manage_booking = generic_api(Booking, BookingSerializer)
manage_payment = generic_api(Payment, PaymentSerializer)
manage_tentcategory=generic_api(TentCategory,TentCategorySerializer)
