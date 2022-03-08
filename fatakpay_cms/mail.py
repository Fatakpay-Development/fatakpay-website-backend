from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


def custom_mail(Subject, Message, To, html_content):
    subject, from_email, to = Subject, 'support@fatakpay.com', To
    text_content = Message
    html_content = html_content
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
