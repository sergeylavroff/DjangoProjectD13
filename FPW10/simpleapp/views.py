from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Product
from datetime import datetime
from .filters import ProductFilter # импортируем недавно написанный фильтр
from .forms import ProductForm


class ProductsListView(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'simpleapp/product_list.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 2
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['form'] = ProductForm(initial={'name': 'Тачка'})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'simpleapp/product_detail.html' # название шаблона будет product.html
    context_object_name = 'product'

class ProductCreateView(CreateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm

class ProductUpdateView(UpdateView):
    template_name = 'simpleapp/product_create.html'
    form_class = ProductForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)

class ProductDeleteView(DeleteView):
    template_name = 'simpleapp/product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'