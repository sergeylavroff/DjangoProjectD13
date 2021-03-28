from django.forms import ModelForm
from .models import News


# Создаём модельную форму
class ArticleForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'