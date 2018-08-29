from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'country', 'std_price', 'price_buy', 'price_sell',
                  'price_send', 'price_receive', 'to_usd')
