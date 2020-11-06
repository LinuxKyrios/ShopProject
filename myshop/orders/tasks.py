from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task sending email notification after successful order creation
    """
    order = Order.objects.get(id=order_id)
    subject = 'Zamówienie nr {}'.format(order.id)
    message = 'Witaj, {}!\m\mZłożyłeś zamówienie w naszym sklepie.\'' \
              'Identyfikator zamówienia to {}.'.format(order.first_name,
                                                       order_id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent