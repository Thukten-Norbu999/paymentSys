from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Account, accNo

@receiver(post_save, sender=CustomUser)
def create_account_for_new_user(sender, instance, created, **kwargs):
    if created:
        account = Account.objects.create(user=instance, account_no=accNo())
        account.generate_qr_code()