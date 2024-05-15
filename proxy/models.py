from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Proxy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='名称', max_length=32)
    http_url = models.CharField(max_length=256, blank=True)
    http_port = models.IntegerField(blank=True, default=0)
    https_url = models.CharField(max_length=256, blank=True)
    https_port = models.IntegerField(blank=True, default=0)
    socks5_url = models.CharField(max_length=256, blank=True)
    socks5_port = models.IntegerField(blank=True, default=0)
    expired_at = models.DateTimeField(verbose_name='过期时间')
    provider = models.CharField(max_length=32, blank=True)
    browser_id = models.CharField(max_length=64, blank=True)
    ads_proxy_id = models.IntegerField(verbose_name='ADC代理Id', blank=True, default=0)
    updated_at = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    description = models.CharField(max_length=256, blank=True)

    class Meta:
        verbose_name = '代理服务信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
