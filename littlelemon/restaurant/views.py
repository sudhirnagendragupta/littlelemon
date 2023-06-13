from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from django.core import serializers
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, 'index.html', {})
# def index(request: HttpRequest) -> HttpResponse:
#     return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
def reservations(request:HttpRequest) -> HttpResponse:
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer    
    
class BookingViewSet(viewsets.ModelViewSet):  
    permission_classes = [IsAuthenticated]  
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
