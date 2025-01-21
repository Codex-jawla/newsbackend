from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    cate_id = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = '__all__'

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    news_id = serializers.ReadOnlyField()
    category = serializers.CharField(source='category.cate_name')
    class Meta:
        model = News
        fields = '__all__'