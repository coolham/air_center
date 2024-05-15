from rest_framework import serializers
from .models import Proxy


class ProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proxy
        # fields = '__all__'  # Include all fields
        fields = ('name', 'http_url', 'http_port', 'https_url', 'https_port', 'socks5_url', 'socks5_port', 'expired_at',
                  'provider', 'browser_id', 'ads_proxy_id', 'updated_at')


# Alternatively, you can specify a list of fields to include/exclude
# fields = ('id', 'name', 'http_url', 'http_port', ...)

# Override field behavior (optional)
# expired_at = serializers.DateTimeField(read_only=True)  # Make expired_at read-only