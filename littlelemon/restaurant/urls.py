#define URL route for index() view
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_api/', views.MenuItemsView.as_view(), name='menuapi'),
    path('reservations/', views.reservations, name="reservations"),
    #APIs
    path('menu_api/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('booking_api/', include(router.urls), name='bookingapi'),
]