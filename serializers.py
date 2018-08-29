from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    country = serializers.CharField(required=False, allow_blank=True, max_length=100)
    std_price = serializers.CharField(required=False, allow_blank=True, max_length=100)
    price_buy = serializers.CharField(required=False, allow_blank=True, max_length=100)
    price_sell = serializers.CharField(required=False, allow_blank=True, max_length=100)
    price_send = serializers.CharField(required=False, allow_blank=True, max_length=100)
    price_receive = serializers.CharField(required=False, allow_blank=True, max_length=100)
    to_usd = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.country = validated_data.get('country', instance.country)
        instance.std_price = validated_data.get('std_price', instance.std_price)
        instance.price_buy = validated_data.get('price_buy', instance.price_buy)
        instance.price_sell = validated_data.get('price_sell', instance.price_sell)
        instance.price_send = validated_data.get('price_send', instance.price_send)
        instance.price_receive = validated_data.get('price_receive', instance.price_receive)
        instance.to_usd = validated_data.get('to_usd', instance.to_usd)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
