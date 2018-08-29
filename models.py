from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())



class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, blank=True, default='')
    std_price = models.CharField(max_length=100, blank=True, default='')
    price_buy = models.CharField(max_length=100, blank=True, default='')
    price_sell = models.CharField(max_length=100, blank=True, default='')
    price_send = models.CharField(max_length=100, blank=True, default='')
    price_receive = models.CharField(max_length=100, blank=True, default='')
    to_usd = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)


