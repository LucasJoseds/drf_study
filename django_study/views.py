
from rest_framework import generics
from django_study.models import Pessoa
from django_study.serializers import PessoaSerializer


class PessoaListCreate(generics.ListCreateAPIView):
    queryset =Pessoa.objects.all()
    serializer_class = PessoaSerializer