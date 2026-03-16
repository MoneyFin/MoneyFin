from rest_framework.views import APIView
from apps.account.models import CustomUser


class CustomUserListAPIViews(APIView):

    def get_queryset():
        return CustomUser.objects.all()


class CustomUserDetailAPIViews(APIView):
    
    def get_queryset():
        return CustomUser.objects.get(id=pk) # NOQA
