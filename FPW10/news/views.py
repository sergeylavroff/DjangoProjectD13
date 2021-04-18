from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .filters import NewsFilter
from .models import News, Category
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives

@login_required
def Subscribe(request, pk ):
    category = get_object_or_404(Category, id=request.POST.get('category'))
    if category.subscriber.filter(id=request.user.id).exists():
        category.subscriber.remove(request.user)
    else:
        category.subscriber.add(request.user)
    return redirect('/news/')


class NewsList(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-creation_date']
    paginate_by = 3


class NewsSearch(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news/newssearch.html'
    context_object_name = 'news'
    ordering = ['-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = 'news/article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        category = News.objects.get(pk=id).category
        context['subscribed'] = False
        if Category.objects.filter(name = category, subscriber = self.request.user ).exists():
            context['subscribed'] = True
        else: context['subscribed'] = False
        return context

class ArticleCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news', )
    template_name = 'news/article_add.html'
    form_class = ArticleForm

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     subscribers = form.instance.category.subscriber.all()
    #     print(subscribers)
    #     address = []
    #     for a in subscribers:
    #         address.append(a.email)
    #     html_content = render_to_string(
    #         'news/article_created.html',
    #         {
    #             'article': form.instance.body,
    #         }
    #     )
    #     msg = EmailMultiAlternatives(
    #         subject=f'{form.instance.title}',
    #         body=form.instance.body,
    #         from_email='center.33@yandex.ru',
    #         to=[ *address ],
    #     )
    #     msg.attach_alternative(html_content, "text/html")  # добавляем html
    #
    #     msg.send()
    #     return super().form_valid(form)

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

