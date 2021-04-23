from celery import shared_task
from .models import News, Category
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from datetime import datetime, timedelta

@shared_task
def notify_subscribers(num, created):
    print(f' Номер новости: {num}')
    instance = News.objects.get( id = int(num) )
    print(instance)
    subscribers = instance.category.subscriber.all()
    address = []
    for a in subscribers:
        address.append(a.email)
    if created:
        subject = f'Новость: {instance.title}'
    else:
        subject = f'Новость изменена: {instance.title}'

    html_content = render_to_string(
        'news/article_created.html',
        {
            'article': instance,
        }
    )
    msg = EmailMultiAlternatives(
        subject,
        body=instance.body,
        from_email='center.33@yandex.ru',
        to=[*address],
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html

    msg.send()

@shared_task
def schedule_notify_subscribers():
    categorys = Category.objects.all()
    for category in categorys:
        subscribers = category.subscriber.all()
        address = []
        for a in subscribers:
            address.append(a.email)
        week_news = News.objects.filter(creation_date__gte=datetime.now()-timedelta(days=7), category = category.id )
        html_content = render_to_string(
            'news/news_schedule.html',
            {
                'news': week_news,
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'Подборка новостей в категории {category.name}',
            body='',
            from_email='center.33@yandex.ru',
            to=[*address],
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()