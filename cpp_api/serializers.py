from rest_framework import serializers
from cpp_api.models import CppApi, LANGUAGE_CHOICES, STYLE_CHOICES


class CppApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CppApi
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')