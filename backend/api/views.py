from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import *
from .serializer import *


# Create your views here.
class CategoryView(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def category(self, request, pk):
        try:
            cate = Category.objects.get(pk=pk)
            emp = News.objects.filter(category=cate)
            newsserializer = NewsSerializer(emp, many=True, context={'request': request})
            return Response(newsserializer.data)
        except Exception as e:
            return Response(f'error no data found {e}')

class NewsView(viewsets.ModelViewSet):
    # parser_classes = (MultiPartParser, FormParser)
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # ordering_fields = ['news_date']

    # def post(self, request, *args, **kwargs):
    #     serializer = NewsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
