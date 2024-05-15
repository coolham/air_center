from django.contrib import admin
from proxy import models


class ProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'browser_id', 'ads_proxy_id', 'http_url', 'http_port', 'https_url', 'https_port',
                    'socks5_url', 'socks5_port', 'expired_at')

admin.site.register(models.Proxy, ProxyAdmin)



