from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer    
    
class BookingViewSet(viewsets.ModelViewSet):  
    permission_classes = [IsAuthenticated]  
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
# class BookingView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
    
    

# class bookingview(APIView):
#     def get(self, request):
#         bookings = Booking.objects.all()
#         serializer = BookingSerializer(bookings, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})
#         return Response(serializer.errors)
    
# class menuview(APIView):
#     def get(self, request):
#         menus = Menu.objects.all()
#         serializer = MenuSerializer(menus, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})
#         return Response(serializer.errors)
    
        