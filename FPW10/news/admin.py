from django.contrib import admin
from .models import News, Category, Author

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Author)