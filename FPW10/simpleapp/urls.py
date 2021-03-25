from django.urls import path
from .views import ProductsList, ProductDetail, Products

urlpatterns = [
    path('old', Products.as_view()),
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view())
]