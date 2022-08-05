"""Views for the prispevok APIs"""
import requests
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView
)

from .models import Prispevok
from .serializers import PostSerializer, PostCreateSerializer


class ListPrispevokAPIView(ListAPIView):
    """Lists all prispevoks from the database"""
    queryset = Prispevok.objects.all()
    serializer_class = PostSerializer


class RetrieveUserAPIView(ListAPIView):
    """Lists all prispevoks for defined user from the database"""
    queryset = Prispevok.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, **kwargs):
        """Retrieve prispevok for user"""
        pk = self.kwargs['pk']
        response = self.queryset.filter(author_id=pk)
        if response:
            return response
        return response


class RetrievePostAPIView(RetrieveAPIView):
    """Lists prispevok according to id from the database"""
    queryset = Prispevok.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, **kwargs):
        """Retrieve prispevok from id"""
        pk = self.kwargs['pk']
        response = self.queryset.filter(id=pk)
        if response:
            return response
        else:
            url = f'https://jsonplaceholder.typicode.com/posts/{pk}'
            r = requests.get(url, headers={'Content-Type': 'application/json'})
            if r.status_code != 200:
                return response
            rest_post = r.json()
            if self.request.user.id == rest_post['userId']:
                Prispevok.objects.create(
                    id=pk, author=self.request.user,
                    title=rest_post['title'], body=rest_post['body']
                )
                return self.queryset.filter(id=pk)
        return response


class CreatePrispevokAPIView(CreateAPIView):
    """Creates a new prispevok"""
    queryset = Prispevok.objects.all()
    serializer_class = PostCreateSerializer


class UpdatePrispevokAPIView(UpdateAPIView):
    """Update the prispevok whose id has been passed through the request"""
    queryset = Prispevok.objects.all()
    serializer_class = PostSerializer


class DeletePrispevokAPIView(DestroyAPIView):
    """Deletes a prispevok whose id has been passed through the request"""
    queryset = Prispevok.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        instance = Prispevok.objects.filter(id=pk)
        if instance:
            instance.delete()
            return Response(f"Prispevok {pk} deleted", )
        else:
            return Response(f"Prispevok {pk} doesn't exist", )
