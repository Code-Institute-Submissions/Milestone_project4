from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart

urlpatterns = [
    path('', view_cart, name = 'view_cart'),
    path('add/<id>', add_to_cart, name = 'add_to_cart'),
    path('remove/<id>', remove_from_cart, name = 'remove_from_cart'),
    path('adjust/<id>', adjust_cart , name='adjust_cart'),
]