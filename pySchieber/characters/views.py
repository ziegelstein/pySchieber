from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Character_Sheet
from .permissions import IsUserOrReadOnly


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Character_Sheet.objects.all()
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = Character_Sheet.objects.all()
    permission_classes = (AllowAny,)
