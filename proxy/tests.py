import pytz
from django.test import TestCase
from rest_framework.test import APIClient
from datetime import datetime, timedelta
from .models import Proxy
from .serializers import ProxySerializer


class ProxyListViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        current_time = datetime.now().replace(tzinfo=pytz.utc)
        expiration_offset = timedelta(days=30)  # Set expiration 30 days from now
        expiration_time = current_time + expiration_offset

        self.proxy1 = Proxy.objects.create(name='proxy1', provider='provider1', socks5_url='192.168.2.1', socks5_port=1080,
                                           browser_id=1,  expired_at=expiration_time),
        self.proxy2 = Proxy.objects.create(name='proxy2', provider='provider2', socks5_url='192.168.2.2', socks5_port=1080,
                                           browser_id=2,  expired_at=expiration_time),

    def test_list_view(self):
        response = self.client.get('/api/proxies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        # Explicitly serialize model instances
        serialized_proxy1 = ProxySerializer(self.proxy1[0]).data
        serialized_proxy2 = ProxySerializer(self.proxy2[0]).data


        # Compare specific fields or use partial matching if needed
        self.assertEqual(response.data[0]['name'], serialized_proxy1['name'])
        self.assertEqual(response.data[0]['provider'], serialized_proxy1['provider'])
        # ... compare other relevant fields ...

        self.assertEqual(response.data[1]['name'], serialized_proxy2['name'])
        self.assertEqual(response.data[1]['provider'], serialized_proxy2['provider'])
        # ... compare other relevant fields ...


class ProductDetailViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        current_time = datetime.now().replace(tzinfo=pytz.utc)
        expiration_offset = timedelta(days=30)  # Set expiration 30 days from now
        expiration_time = current_time + expiration_offset

        self.proxy1 = Proxy.objects.create(name='proxy1', provider='provider1', socks5_url='192.168.2.1', socks5_port=1080,
                                           browser_id=1,  expired_at=expiration_time),

    def test_detail_view(self):
        response = self.client.get('/api/proxies/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, ProxySerializer(self.proxy1[0]).data)
