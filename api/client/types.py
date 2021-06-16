import graphene
from graphene_django import DjangoObjectType
from api.client.model import Client


class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'rg_number', 'rg_state', 'cpf', 'apartment')

