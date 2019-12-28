from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ProfileUser


def create_profile(sender, **kwargs):

    if kwargs['created']:
        profile = ProfileUser.objects.create(user = kwargs['instance'])
        print('yes!, created')


post_save.connect(create_profile , sender = User)

# @receiver(post_save, sender = User)
# def create_profile(sender , instance, created, **kwargs):
#     if created:
#         ProfileUser.objects.create(user = instance)
#         print('created')



# @receiver(post_save, sender = User)
# def save_profile(sender, instance, **kwargs):
#     instance.profileuser.save()
