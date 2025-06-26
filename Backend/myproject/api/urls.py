from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import viewsets
from myapp.views import * # type: ignore

urlpatterns = [
    # USER
    path('users/', manage_user, name='manage_user'),
    path('users/<int:id>/', manage_user, name='manage_user_detail'),

    # TENT CATEGORY
    path('tentcategories/', manage_tentcategory, name='manage_tentcategory'),
    path('tentcategories/<int:id>/', manage_tentcategory, name='manage_tentcategory_detail'),

    # EVENTS
    path('events/', manage_event, name='manage_event'),
    path('events/<int:id>/', manage_event, name='manage_event_detail'),

    # BOOKINGS
    path('bookings/', manage_booking, name='manage_booking'),
    path('bookings/<int:id>/', manage_booking, name='manage_booking_detail'),

    # PAYMENTS
    path('payments/', manage_payment, name='manage_payment'),
    path('payments/<int:id>/', manage_payment, name='manage_payment_detail'),
]

# Static/media file serving (important if using file/image uploads)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
