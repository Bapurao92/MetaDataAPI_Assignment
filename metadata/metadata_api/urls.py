from django.conf.urls import url
from django.urls import path, include
from views.metadata_view import (
    MetaDataApiView,
)

urlpatterns = [
    path('api', MetaDataApiView.as_view()),
]
