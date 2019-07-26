from rest_framework import serializers
from .models import Common, Detail

# 공통 정보 조회
class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = '__all__'

# 전체 정보 조회
class DetailSerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'

# 지역코드로 정보 조회
class SearchByAreaSerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'

# 지역코드, 시군구코드로 정보 조회
class SearchBySigunguSerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'

# 항목으로 정보 조회
class SearchByCategorySerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'

# contentId로 정보 조회
class SearchByContentIdSerializer(serializers.ModelSerializer):
    common = CommonSerializer(source='common_set', many=True, read_only=True)
    class Meta:
        model = Detail
        fields = '__all__'