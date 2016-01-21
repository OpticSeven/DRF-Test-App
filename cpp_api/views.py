from cpp_api.models import CppApi
from cpp_api.serializers import CppApiSerializer, UserSerializer
from rest_framework import generics, renderers
from django.contrib.auth.models import User
from rest_framework import permissions
from cpp_api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('cppapi-list', request=request, format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    queryset = CppApi.objects.all()
    serializer_class = CppApiSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CppApi.objects.all()
    serializer_class = CppApiSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetHighlight(generics.GenericAPIView):
    queryset = CppApi.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)