from rest_framework import serializers
# from .models import DetailInform

class DetailInformSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailInform
        fields = '__all__'