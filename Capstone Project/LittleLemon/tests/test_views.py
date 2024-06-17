from django.test import TestCase
from rest_framework.test import APIClient
from LittleLemonApp.models import MenuItem
from LittleLemonApp.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(title="Burger", price=10.99, inventory=50)
        self.menu_item2 = MenuItem.objects.create(title="Pizza", price=12.99, inventory=40)
    
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)