from rest_framework import serializers
from cpp_api.models import CppApi, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class CppApiSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='cppapi-highlight', format='html')

    class Meta:
        model = CppApi
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cpp_api = serializers.HyperlinkedRelatedField(many=True, view_name='cppapi-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'cpp_api')
