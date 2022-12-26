# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from api.models import CustomUser,UserType
#
#
# @receiver(pre_save, sender=CustomUser)
# def create_user_type(sender, instance, **kwargs):
#     """This signal sets user type to buyer when a user is saved for the first time."""
#     user_type_obj=UserType.objects.create(user_type='buyer')
#     instance.user_type=user_type_obj.id
