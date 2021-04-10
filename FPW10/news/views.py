from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import NewsFilter
from .models import News
from .forms import ArticleForm


class NewsList(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-creation_date']
    paginate_by = 3

class NewsSearch(ListView):
    model = News
    template_name = 'news/newssearch.html'
    context_object_name = 'news'
    ordering = ['-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ArticleDetailView(DetailView):
    model = News
    template_name = 'news/article.html'
    context_object_name = 'article'

class ArticleCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news', )
    template_name = 'news/article_add.html'
    form_class = ArticleForm

class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_news', )
    template_name = 'news/article_add.html'
    form_class = ArticleForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)

class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_news', )
    template_name = 'news/article_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'