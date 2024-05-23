from django.conf.urls import url
from django.urls import path, include
from views.metadata_view import (
    MetaDataCreateApiView,
    MetaDataRetrieveByLocationView,
    MetaDataRetrieveByDepartmentView,
    MetaDataRetrieveByCategoryView,
    MetaDataRetrieveBySubCategoryView,
    MetaDataUpdateByLocationView,
    MetaDataDeleteByLocationView
)

urlpatterns = [
    path('api/create', MetaDataCreateApiView.as_view()),
    path('api/retrieve_location', MetaDataRetrieveByLocationView.as_view()),
    path('api/retrieve_department', MetaDataRetrieveByDepartmentView.as_view()),
    path('api/retrieve_category', MetaDataRetrieveByCategoryView.as_view()),
    path('api/retrieve_sub_category', MetaDataRetrieveBySubCategoryView.as_view()),
    path('api/update', MetaDataUpdateByLocationView.as_view()),
    path('api/delete', MetaDataDeleteByLocationView.as_view())
]
