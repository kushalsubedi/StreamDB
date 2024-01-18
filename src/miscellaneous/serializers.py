from rest_framework import serializers

from . import models

class FAQserializer(serializers.ModelSerializer):
    class Meta:
        fields = ('question', 'answer')
        model = models.FAQ

class FAQ_Details_serializer(serializers.ModelSerializer):
    class Meta:
        fields = ('question', 'answer','created_date','created_by','updated_date')
        model = models.FAQ


class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TermsAndConditions
        fields = ('title', 'content', 'created_at')

class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrivacyPolicy
        fields = ('title', 'content', 'created_at')