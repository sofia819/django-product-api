from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product_details', views.ProductDetailsView)

urlpatterns = [
    # router generates urls for us automatically
    path('', include(router.urls))
]
