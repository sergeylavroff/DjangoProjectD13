from django.urls import path
from .views import NewsList, ArticleDetailView, NewsSearch, ArticleCreateView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path('', NewsList.as_view()),
    path('search', NewsSearch.as_view()),
    path('<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('add', ArticleCreateView.as_view(), name='article_create')
]
