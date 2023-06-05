#define URL route for index() view
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('booking/', include(router.urls)),
]