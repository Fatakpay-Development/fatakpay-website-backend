from django.core.mail import send_mail
def custom_mail(Subject, Message, To):
    print("data")
    print(Subject)
    print(Message)
    print(To)
    print("data")
    # send_mail(
    #     Subject,
    #     Message,
    #     'support@idoot.in',
    #     To,
    # )