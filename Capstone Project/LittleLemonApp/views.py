from django.shortcuts import render
from .models import MenuItems
from .serializers import MenuItemsSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsVIew(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer