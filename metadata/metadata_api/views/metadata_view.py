from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from models.metadata_model import Loocation, Department, Category, SubCategory
from serializers import metadata_serializer


class MetaDataCreateApiView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Create the MetaData with given data
        """
        data = {
            'location': request.data.get('location'),
            'department': request.data.get('department'),
            'category': request.data.get('category'),
            'sub category': request.data.get('sub category')
        }
        serializer = metadata_serializer.MetaDataCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MetaDataRetrieveByLocationView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        serializer = metadata_serializer.MetaDataRetrieveByLocationSerializer(request.location)
        records = MetaData.objects.filter(location=request.data.get("location"))
        return Response(records, status=status.HTTP_200_OK)


class MetaDataRetrieveByDepartmentView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        serializer = metadata_serializer.MetaDataRetrieveByDepartmentSerializer(request.department)
        records = MetaData.objects.filter(department=request.data.get("department"))
        return Response(records, status=status.HTTP_200_OK)


class MetaDataRetrieveByCategoryView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        serializer = metadata_serializer.MetaDataRetrieveByCategorySerializer(request.category)
        records = MetaData.objects.filter(category=request.data.get("category"))
        return Response(records, status=status.HTTP_200_OK)


class MetaDataRetrieveBySubCategoryView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        serializer = metadata_serializer.MetaDataRetrieveBySubCategorySerializer(request.subCategory)
        records = MetaData.objects.filter(sub_category=request.data.get("Sub Category"))
        return Response(records, status=status.HTTP_200_OK)


class MetaDataUpdateByLocationView(APIView):

    # 1. List all
    def put(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        data = {
            'location': request.data.get('location'),
            'department': request.data.get('department'),
            'category': request.data.get('category'),
            'sub category': request.data.get('sub category')
        }
        serializer = metadata_serializer.MetaDataUpdateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MetaDataDeleteByLocationView(APIView):

    # 1. List all
    def delete(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        serializer = metadata_serializer.MetaDataDeleteByLocationSerializer(request.data)
        records = MetaData.objects.delete(location=request.data.get("location"))
        return Response(records, status=status.HTTP_200_OK)
