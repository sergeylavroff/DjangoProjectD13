from django.urls import path
from .views import NewsList, ArticleDetailView, NewsSearch, ArticleCreateView, ArticleDeleteView, ArticleUpdateView, Subscribe
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('', cache_page(60)(NewsList.as_view()), name='start'),
    path('search', cache_page(60*5)(NewsSearch.as_view())),
    path('<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('add', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/subscribe/', Subscribe, name='subscribe'),
]
