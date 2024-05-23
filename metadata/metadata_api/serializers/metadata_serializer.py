from rest_framework import serializers
from .models import Location, Department, Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = '__all__'


class MetaDataCreateSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=50)
    department = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=200)
    sub_category = serializers.CharField(max_length=200)


class MetaDataRetrieveByLocationSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=50)


class MetaDataRetrieveByDepartmentSerializer(serializers.ModelSerializer):
    department = serializers.CharField(max_length=100)


class MetaDataRetrieveByCategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=200)


class MetaDataRetrieveBySubCategorySerializer(serializers.ModelSerializer):
    sub_category = serializers.CharField(max_length=200)


class MetaDataUpdateSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=50)
    department = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=200)
    sub_category = serializers.CharField(max_length=200)


class MetaDataDeleteByLocationSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=50)
