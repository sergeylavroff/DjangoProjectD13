from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from .models import News
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=News)
def notify_subscribers(sender, instance, created, **kwargs):
    subscribers = instance.category.subscriber.all()
    print(subscribers)
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

