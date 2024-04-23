from django.urls import path
from .views import AddresourceView
from .views import ResourceListAPI

urlpatterns = [
    
    path('add_price/', AddresourceView.as_view(), name='add-content'),
    path('view_pricess/', ResourceListAPI.as_view(), name='get_course'),
    
]