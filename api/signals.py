from api.models import UserType,CustomUser
from rest_framework.exceptions import status


def create_user_type(sender, instance, **kwargs):
    """This signal sets user type to buyer when a user is saved for the first time."""
    try:
        UserType.objects.create(user_id=instance)
    except Exception as e:
        print('create user signal ', e, status.HTTP_500_INTERNAL_SERVER_ERROR)
        # instance.delete()
