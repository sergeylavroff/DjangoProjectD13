from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from .models import News
from .tasks import notify_subscribers

@receiver(post_save, sender=News)
def notify_via_celery(sender, instance, created, **kwargs):
    # print(sender)
    # print(instance.id)
    # print(created)
    num = instance.id
    notify_subscribers.delay(num, created)

