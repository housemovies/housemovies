
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.ModelViewSetClass import ModelViewSetClass
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action

from principal.models import Menu, Pelicula, MenuPelicula
from principal.serializers import UserFindSerializer, UserLoginSerializer, MenuSerializer, MenuPeliculaSerializer, PeliculaSerializer
import pdb

class MenuViewSet(ModelViewSetClass):
    # permission_classes = ()
    queryset = Menu.objects.filter(delete=None)
    serializer_class = MenuSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['nombre']

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        data = MenuSerializer(query, many=True).data
        return Response(data)


class MenuPeliculaViewSet(ModelViewSetClass):
    queryset = MenuPelicula.objects.filter(delete=None)
    serializer_class = MenuPeliculaSerializer

    def retrieve(self, request, *args, **kwargs):
        item = MenuPelicula.objects.filter(menu_id=kwargs['pk'])
        # pdb.set_trace()
        page = self.paginate_queryset(item)
        serializer = MenuPeliculaSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)



class PeliculaViewSet(ModelViewSetClass):
    queryset = Pelicula.objects.filter(delete=None).order_by('-vistas')
    serializer_class = PeliculaSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['nombre']

    @action(methods=['get'], detail=False,url_path='ultimas')
    def ultimas(self, request ): 
        query = self.get_queryset().order_by('-created')[:15]
        data = PeliculaSerializer(query, many=True).data
        return Response(data)

    @action(methods=['get'], detail=False,url_path='carousel')
    def carousel(self, request ): 
        query = self.get_queryset().filter(carousel=True).order_by('-created')[:15]
        data = PeliculaSerializer(query, many=True).data
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        obj_pelicula = Pelicula.objects.get(pk=kwargs['pk'])
        obj_pelicula.vistas = obj_pelicula.vistas + 1
        obj_pelicula.save()
        serializer = PeliculaSerializer(obj_pelicula)
        return Response(serializer.data)



























class UserViewGet(APIView):
    def get(self, request, ):
        data = UserFindSerializer(request.user).data
        return Response(data)


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserFindSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    def post(self, request, ):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)