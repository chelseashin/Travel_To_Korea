from rest_framework import serializers
from .models import Common, Detail

class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'

class SearchByAreaSerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'

class SearchBySigunguSerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'

class SearchByCategorySerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'

class SearchByContentIdSerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'