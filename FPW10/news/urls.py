from django.urls import path
from .views import NewsList, ArticleDetail

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', ArticleDetail.as_view())
]